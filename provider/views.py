from .modules import *

# Create your views here.



@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_multiple_images(request):
    images = request.FILES.getlist('images')  # Get multiple files from the request
    image_names = request.data.getlist('image_names', [])  # Optional: Names for images
    image_descriptions = request.data.getlist('image_descriptions', [])  # Optional: Descriptions for images

    if not images:
        return Response({'error': 'No images provided'}, status=status.HTTP_400_BAD_REQUEST)

    created_images = []

    # Iterate over the images and create ProductImage instances
    for idx, image in enumerate(images):
        image_name = image_names[idx] if len(image_names) > idx else None
        image_description = image_descriptions[idx] if len(image_descriptions) > idx else None

        # Create a new ProductImage instance
        product_image = ProductImage.objects.create(
            ImageUrl=image,
            ImageName=image_name,
            ImageDescription=image_description
        )
        created_images.append(product_image)

    # Serialize the created images and return them in the response
    serializer = ProductImageSerializer(created_images, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)




