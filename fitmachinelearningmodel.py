model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['acc'])

train=model.fit_generator(
    generatingtraining,
    epochs=10,
    validation_data=generatingtesting                          
)
