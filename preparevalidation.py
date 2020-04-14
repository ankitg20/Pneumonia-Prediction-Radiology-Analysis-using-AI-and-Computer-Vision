directoryvalid='../input/chest-xray-pneumonia/chest_xray/chest_xray/val'
genvalid=train_gen.flow_from_directory(validation_dir, class_mode='binary')
