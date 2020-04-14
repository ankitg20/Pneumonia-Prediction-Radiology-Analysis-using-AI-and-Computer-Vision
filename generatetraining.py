generatingtraining=tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            horizontal_flip=True)

generatingtesting=tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            horizontal_flip=True)

directoryoftraining='../input/chest-xray-pneumonia/chest_xray/chest_xray/train'
generatetraining=train_gen.flow_from_directory(
                train_dir,
                class_mode='binary')
