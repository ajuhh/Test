# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Product, SubVariant, StockTransaction
# from .serializers import ProductSerializer, StockTransactionSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.prefetch_related('variants__sub_variants')
#     serializer_class = ProductSerializer

#     # def create(self, request):
#     #     # Add variants to context for custom create method
#     #     serializer = self.get_serializer(
#     #         data=request.data, 
#     #         context={'variants': request.data.get('variants', [])}
#     #     )
#     #     serializer.is_valid(raise_exception=True)
#     #     self.perform_create(serializer)
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#     def create(self, request):
#     # Add variants to context for custom create method
#     serializer = self.get_serializer(
#         data=request.data,
#         context={'variants': request.data.get('variants', [])}
#     )
#     serializer.is_valid(raise_exception=True)  # Validate input
#     self.perform_create(serializer)  # Save the new product

#     return Response(serializer.data, status=status.HTTP_201_CREATED)


#     @action(detail=False, methods=['GET'])
#     def list_products(self, request):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
        
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
        
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     @action(detail=False, methods=['POST'])
#     def add_stock(self, request):
#         sub_variant_id = request.data.get('sub_variant_id')
#         quantity = request.data.get('quantity')
        
#         try:
#             sub_variant = SubVariant.objects.get(id=sub_variant_id)
            
#             # Create stock transaction
#             transaction_data = {
#                 'sub_variant': sub_variant_id,
#                 'quantity': quantity,
#                 'transaction_type': 'purchase',
#                 'user': request.user.id
#             }
            
#             transaction_serializer = StockTransactionSerializer(data=transaction_data)
#             if transaction_serializer.is_valid():
#                 transaction_serializer.save()
                
#                 # Update stock
#                 sub_variant.stock += float(quantity)
#                 sub_variant.save()
                
#                 # Update total product stock
#                 product = sub_variant.variant.product
#                 product.TotalStock = sum(
#                     sv.stock for v in product.variants.all() 
#                     for sv in v.sub_variants.all()
#                 )
#                 product.save()
                
#                 return Response({'message': 'Stock added successfully'}, status=status.HTTP_200_OK)
            
#             return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         except SubVariant.DoesNotExist:
#             return Response({'error': 'Sub Variant not found'}, status=status.HTTP_404_NOT_FOUND)

#     @action(detail=False, methods=['POST'])
#     def remove_stock(self, request):
#         sub_variant_id = request.data.get('sub_variant_id')
#         quantity = request.data.get('quantity')
        
#         try:
#             sub_variant = SubVariant.objects.get(id=sub_variant_id)
            
#             # Check if sufficient stock
#             if sub_variant.stock < float(quantity):
#                 return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)
            
#             # Create stock transaction
#             transaction_data = {
#                 'sub_variant': sub_variant_id,
#                 'quantity': quantity,
#                 'transaction_type': 'sale',
#                 'user': request.user.id
#             }
            
#             transaction_serializer = StockTransactionSerializer(data=transaction_data)
#             if transaction_serializer.is_valid():
#                 transaction_serializer.save()
                
#                 # Update stock
#                 sub_variant.stock -= float(quantity)
#                 sub_variant.save()
                
#                 # Update total product stock
#                 product = sub_variant.variant.product
#                 product.TotalStock = sum(
#                     sv.stock for v in product.variants.all() 
#                     for sv in v.sub_variants.all()
#                 )
#                 product.save()
                
#                 return Response({'message': 'Stock removed successfully'}, status=status.HTTP_200_OK)
            
#             return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         except SubVariant.DoesNotExist:
#             return Response({'error': 'Sub Variant not found'}, status=status.HTTP_404_NOT_FOUND)
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, SubVariant, StockTransaction
from .serializers import ProductSerializer, StockTransactionSerializer



class ProductViewSet(viewsets.ModelViewSet):
    # This is the queryset to fetch the products and their related data
    queryset = Product.objects.prefetch_related('variants__sub_variants')
    serializer_class = ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    # Custom create method for creating a product and its variants
    # def create(self, request):
    #     # Add variants to context for custom create method
    #     serializer = self.get_serializer(
    #         data=request.data,
    #         context={'variants': request.data.get('variants', [])}  # Passing variants data
    #     )
    def create(self, request, *args, **kwargs):
        print("Received data:", request.data)  # Log incoming data
        return super().create(request, *args, **kwargs)
        
        serializer.is_valid(raise_exception=True)  # Validate the data
        self.perform_create(serializer)  # Save the product

        # Return the created product's data in the response
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.prefetch_related('variants__sub_variants')
#     serializer_class = ProductSerializer

#     def create(self, request):
#         # Pass variants to context for custom create method
#         serializer = self.get_serializer(
#             data=request.data,
#             context={'variants': request.data.get('variants', [])}
#         )
        
#         if serializer.is_valid():
#             self.perform_create(serializer)  # Save the product and its variants
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom action to list all products
    @action(detail=False, methods=['GET'])
    def list_products(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Custom action to add stock to a product
    @action(detail=False, methods=['POST'])
    def add_stock(self, request):
        sub_variant_id = request.data.get('sub_variant_id')
        quantity = request.data.get('quantity')

        try:
            sub_variant = SubVariant.objects.get(id=sub_variant_id)

            # Create stock transaction
            transaction_data = {
                'sub_variant': sub_variant_id,
                'quantity': quantity,
                'transaction_type': 'purchase',
                'user': request.user.id
            }

            transaction_serializer = StockTransactionSerializer(data=transaction_data)
            if transaction_serializer.is_valid():
                transaction_serializer.save()

                # Update stock of the subvariant
                sub_variant.stock += float(quantity)
                sub_variant.save()

                # Update the total stock for the product
                product = sub_variant.variant.product
                product.TotalStock = sum(
                    sv.stock for v in product.variants.all() 
                    for sv in v.sub_variants.all()
                )
                product.save()

                return Response({'message': 'Stock added successfully'}, status=status.HTTP_200_OK)

            return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except SubVariant.DoesNotExist:
            return Response({'error': 'Sub Variant not found'}, status=status.HTTP_404_NOT_FOUND)

    # Custom action to remove stock from a product
    @action(detail=False, methods=['POST'])
    def remove_stock(self, request):
        sub_variant_id = request.data.get('sub_variant_id')
        quantity = request.data.get('quantity')

        try:
            sub_variant = SubVariant.objects.get(id=sub_variant_id)

            # Check if there's enough stock to remove
            if sub_variant.stock < float(quantity):
                return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)

            # Create stock transaction for sale
            transaction_data = {
                'sub_variant': sub_variant_id,
                'quantity': quantity,
                'transaction_type': 'sale',
                'user': request.user.id
            }

            transaction_serializer = StockTransactionSerializer(data=transaction_data)
            if transaction_serializer.is_valid():
                transaction_serializer.save()

                # Update stock of the subvariant
                sub_variant.stock -= float(quantity)
                sub_variant.save()

                # Update the total stock for the product
                product = sub_variant.variant.product
                product.TotalStock = sum(
                    sv.stock for v in product.variants.all() 
                    for sv in v.sub_variants.all()
                )
                product.save()

                return Response({'message': 'Stock removed successfully'}, status=status.HTTP_200_OK)

            return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except SubVariant.DoesNotExist:
            return Response({'error': 'Sub Variant not found'}, status=status.HTTP_404_NOT_FOUND)
