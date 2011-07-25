/* @pjs pauseOnBlur="true"; */
//screen min and max
float[] smin = {0, 0};
float[] smax = {600, 480};
//background image
PImage bg_image;

void setup() 
{
	  size(smax[0], smax[1]);
	  //size(smax[0], smax[1], OPENGL);
    //don't loop for now
    //noLoop();
    frameRate(30);
	  //bg_image = loadImage("bg.png");
}

void draw() 
{
    //backgrond color. clears the scene
    background(200, 200, 200, 255);
    colorMode(RGB,255,255,255,255);
	  //image(bg_image, 0, 0); 
    
    //draw a rectangle with no border
    noStroke();
    fill(0, 255, 0);
    rect(200, 200, 50, 100);

    //draw a rectangle with a border
    stroke(100, 100, 100);
    fill(0, 255, 0);
    rect(400, 200, 50, 100);

    //draw a rectangle with it's dimensions taken from javascript specified in index.html
    fill(0, 0, 255);
    rect(300, 400, testFromJS, testFromJS);
    console.log("test from js: " + testFromJS);

}

void keyPressed()
{
  console.log(key);
  if(key == 'p')
  {
    console.log("do something because p was pressed");
  }
  if(key == 'e')
  {

  }
}

/*
void mousePressed() 
{
  //ya.restart();
  //console.log(mouseX + " " + mouseY);
}
*/

void mouseMoved()
{
  stroke(200, 100, 100);
  fill(255, 0, 0);
  ellipse(mouseX, mouseY, 15, 15);
}
