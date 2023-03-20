# Airfoil_pressure_level_prediction

This model predicts scaled sound pressure level on airfoils of a space shuttle at various wind tunnel speeds and angles of attack.


## Run Locally

To Locally run the project follow these instructions:

Clone the project

```bash
  git clone https://github.com/Swaraj-6/Airfoil_pressure_level_prediction.git
```

Go to the project directory

```bash
  cd my-project
```

Install all dependencies and packages with specified versions

```bash
  pip install .\requirements.txt
```

Start the server

```bash
  python .\app.py
```


## Running Tests

To run tests, you can copy this url
http://127.0.0.1:5000 and paste it in browser, on homepage you have to put all of the following inputs:

1. Frequency, in Hertzs.
2. Angle of attack, in degrees.
3. Chord length, in meters.
4. Free-stream velocity, in meters per second.
5. Suction side displacement thickness, in meters.

and below your sound pressure level in decibels will appear.

Or you can run test in api using postman application, for that follow these steps:
1. http://127.0.0.1:5000/api paste this url on postman and put the request to "POST" method
2. Then go to body section.
3. Choose json as input (as any other form of input is not applicable).
4. There you have to make a json of following manner:

```
  {
    "Frequency":1300,
    "Angle_of_attack":25.5,
    "Chord_length":0.0254,
    "F-S_velocity":71.3,
    "Suction_side":0.016104
}
```
5. Then you can go ahead and send the request and you will see your output.

## Demo



