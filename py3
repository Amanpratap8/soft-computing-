model = Sequential()
model.add(Dense(256, input_shape=(len(train_x[0]),),
				activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))


sgd = SGD(learning_rate=0.01, decay=1e-6,
		momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
			optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y),
				epochs=200, batch_size=5, verbose=1)

model.save("chatbot_model.h5", hist)
print("Done!")
