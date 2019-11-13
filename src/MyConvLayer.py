import keras


# TODO finish
#model.add(Conv2D(32, KERNEL_SIZE, input_shape=INPUT_SHAPE))
#model.add(Activation(ACTIVATION_HIDDEN_LAYERS))
#model.add(MaxPooling2D(pool_size=POOL_SIZE))

# #Conv2D -> Activation -> MaxPooling2D
class MyConvLayer(keras.layers.Layer):
    def __init__(self, filters, kernel_size, input_shape, pool_size=(2,2), activation='relu', **kwargs):
        super().__init__(**kwargs)
        self.filters = filters
        self.kernel_size = kernel_size
        self.input_shape = input_shape
        self.pool_size = pool_size
        self.activation = activation