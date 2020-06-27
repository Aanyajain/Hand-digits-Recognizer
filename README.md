# Hand-digits-Recognizer
This project helps to identify the hadnwriiten letters or alphabets.
It is trained using MNIST(Modified National Institute of Standards and Tech database):large database of handwritten digits used to train various image processing systems.
Then we trained our Neural Network by MLPClassifier using Backpropagation method on Mnist dataset.Then we test our model by writing digits in GIMP(GNU Image Manipulation Platform) and then export that file in another file which converts that image to bytes.
Thn the bytes converted to matrix which is then predicted using our model.
Hence our output digit is predicted.
