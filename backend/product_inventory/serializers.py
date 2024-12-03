# from rest_framework import serializers
# from .models import Product, Variant, SubVariant, StockTransaction

# class SubVariantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubVariant
#         fields = ['option', 'stock']

# class VariantSerializer(serializers.ModelSerializer):
#     sub_variants = SubVariantSerializer(many=True)

#     class Meta:
#         model = Variant
#         fields = ['name', 'sub_variants']

# class ProductSerializer(serializers.ModelSerializer):
#     variants = VariantSerializer(many=True, required=False)

#     class Meta:
#         model = Product
#         fields = '__all__'
#         read_only_fields = ['id', 'CreatedDate', 'TotalStock']

#     def create(self, validated_data):
#         variants_data = self.context.get('variants', [])
        
#         # Create Product
#         product = Product.objects.create(**validated_data)
        
#         # Create Variants and SubVariants
#         for variant_data in variants_data:
#             variant = Variant.objects.create(
#                 product=product, 
#                 name=variant_data['name']
#             )
            
#             for option in variant_data.get('options', []):
#                 SubVariant.objects.create(
#                     variant=variant, 
#                     option=option
#                 )
        
#         return product

# class StockTransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StockTransaction
#         fields = '__all__'
#         read_only_fields = ['timestamp']











# # from rest_framework import serializers
# # from .models import Product, Variant, SubVariant
# # from .models import StockTransaction 

# # class StockTransactionSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = StockTransaction
# #         fields = '__all__'

# # class SubVariantSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = SubVariant
# #         fields = ['option', 'stock']


# # class VariantSerializer(serializers.ModelSerializer):
# #     sub_variants = SubVariantSerializer(many=True)

# #     class Meta:
# #         model = Variant
# #         fields = ['name', 'sub_variants']


# # class ProductSerializer(serializers.ModelSerializer):
# #     variants = VariantSerializer(many=True, required=False)

# #     class Meta:
# #         model = Product
# #         fields = '__all__'
# #         read_only_fields = ['id', 'CreatedDate', 'TotalStock']

# #     def create(self, validated_data):
# #         variants_data = self.context.get('variants', [])

# #         # Create Product
# #         product = Product.objects.create(**validated_data)

# #         # Create Variants and SubVariants
# #         for variant_data in variants_data:
# #             variant = Variant.objects.create(
# #                 product=product,
# #                 name=variant_data['name']
# #             )

# #             for option in variant_data.get('options', []):
# #                 SubVariant.objects.create(
# #                     variant=variant,
# #                     option=option
# #                 )

# #         return product

from rest_framework import serializers
from .models import Product, Variant, SubVariant, StockTransaction

class SubVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubVariant
        fields = ['option', 'stock']

class VariantSerializer(serializers.ModelSerializer):
    sub_variants = SubVariantSerializer(many=True, required=False)

    class Meta:
        model = Variant
        fields = ['name', 'sub_variants']

class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'CreatedDate', 'TotalStock']

    def create(self, validated_data):
        # Extract nested data
        variants_data = validated_data.pop('variants', [])

        # Create the Product instance
        product = Product.objects.create(**validated_data)

        # Create Variants and SubVariants
        for variant_data in variants_data:
            sub_variants_data = variant_data.pop('sub_variants', [])
            variant = Variant.objects.create(product=product, **variant_data)

            for sub_variant_data in sub_variants_data:
                SubVariant.objects.create(variant=variant, **sub_variant_data)

        return product

    def update(self, instance, validated_data):
        # Extract nested data
        variants_data = validated_data.pop('variants', None)

        # Update the Product instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if variants_data is not None:
            # Clear existing variants and sub_variants
            instance.variants.all().delete()

            # Create new variants and sub_variants
            for variant_data in variants_data:
                sub_variants_data = variant_data.pop('sub_variants', [])
                variant = Variant.objects.create(product=instance, **variant_data)

                for sub_variant_data in sub_variants_data:
                    SubVariant.objects.create(variant=variant, **sub_variant_data)

        return instance

class StockTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTransaction
        fields = '__all__'
        read_only_fields = ['timestamp']

