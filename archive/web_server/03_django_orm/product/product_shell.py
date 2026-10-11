from datetime import datetime, timedelta
from django.utils import timezone

reivews = Review.objects.filter(product_id=1)
reivews
for review in reviews:
    print(review.id, review.product, review.user_id)

product = Product.objects.get(id=1)
Review.objects.filter(product=product)

product.reviews
product.reviews.all()

product = Product.objects.get(id=1)
average_rating = product.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
review_count = product.reviews.count()
print(f'priduct id 1의 평균 평점: {average_rating}, 리뷰 수: {review_count}')

high_rating_reviews = product.reviews.filter(rating__gte=4)
for review in high_rating_reviews:
    print(review.id, review.product, review.user_id, review.rating, review.comment)

products_with_review_data = Product.objects.annotate(
    average_rating = Avg('reviews_rating'),
    review_count = Count('reviews')
)
products_with_review_data

for product in products_with_review_data:
    avg_rating = f'{product.avg_raing:.2f}' if product.avg_rating else '0'
    print(f'Product: {product.name}, Average Rating: {avg_rating}, Reviews: {product.review_count}')

start_date = timezone.now() - timedelta(weeks=1)
end_date = timezone.now()
reviews = Review.objects.filter(created_at__range=(start_date, end_date))
for review in reviews:
    print(review.id, review.product, review.user_id, review.rating, review.comment)

