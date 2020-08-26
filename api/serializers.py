from rest_framework import serializers

from .models import Category, Comment, Genre, Review, Title, User


class CategorySerializer(serializers.ModelSerializer):
    '''Сериализатор для категорий (типов) произведений'''
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    '''Сериализатор для жанров'''
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleCreateSerializer(serializers.ModelSerializer):
    '''Сериализатор для добавления произведений'''
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all())

    class Meta:
        fields = ('id', 'name', 'year', 'genre', 'category', 'description')
        model = Title


class TitleListSerializer(serializers.ModelSerializer):
    '''Сериализатор для возврата списка произведений'''
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.FloatField()

    class Meta:
        fields = ('id', 'name', 'year', 'genre',
                  'rating', 'category', 'description')
        model = Title


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор модели пользователя'''
    class Meta:
        model = User
        fields = ('id', 'username', 'role', 'email',
                  'first_name', 'last_name', 'bio')


class ReviewSerializer(serializers.ModelSerializer):
    '''Сериализатор модели отзывов'''
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    def validate(self, attrs):
        request = self.context['request']
        if request.method != 'POST':
            return attrs

        title = Title.objects.filter(
            pk=self.context['view'].kwargs.get('title')).exists()
        if not title:
            return attrs

        title = Title.objects.get(pk=self.context['view'].kwargs.get('title'))
        review = Review.objects.filter(
            author=request.user).filter(title=title).exists()
        if review:
            raise serializers.ValidationError(
                  'One user can make only one review per title.')
        return attrs

    class Meta:
        model = Review
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    '''Сериализатор модели комментариев'''
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'review_id', 'text', 'author', 'pub_date')
