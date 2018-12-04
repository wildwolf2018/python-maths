'''
Draws the Mandelbrot set with 400 equally spaced points
along the x and y-axis
'''
import matplotlib.pyplot as plt   
import matplotlib.cm as cm            

def initialize_image(x_numPoints, y_numPoints):       
	image = []                        
	for i in range(y_numPoints):             
		x_colors = []                     
		for j in range(x_numPoints):                 
			x_colors.append(0)            
		image.append(x_colors)        
	return image 

def create_mandelbrot_set(x_numPoints, y_numPoints, max_iteration, canvas):
	width = 110 #Width of the image
	x_dist = 1 / width #Distance between two points along the x-axis
	height = 200 #Height of the image
	y_dist = 1 / height #Distance between two points along the y-axis
	start_x = -2.5 #Minimum x coordinate value
	start_y = -1.0 #Minimum y coordinate value

	for i in range(y_numPoints):
	 	for k in range(x_numPoints):
	 		z1 = 0 + 0j
	 		real = start_x + k * x_dist
	 		img = start_y + i * y_dist
	 		c = complex(real, img)
	 		iteration = 0	
	 		while abs(z1) < 2 and iteration < max_iteration:
	 			z1 = z1 ** 2 + c
	 			iteration = iteration + 1
 			canvas[i][k] = iteration
	return canvas

if __name__ == '__main__':
	x_numPoints = 400    #Number of equally spaced point on the x-axis          
	y_numPoints = 400    #Number of equally spaced point on the y-axis
	max_iteration = 1000 #Maximum number of allowed iterations                      
	image = initialize_image(x_numPoints, y_numPoints) 
	image = create_mandelbrot_set(x_numPoints, y_numPoints, max_iteration, image)

	#Plots the Mandelbrot set on the x-y axis
	plt.imshow(image, origin='lower', extent=(-2.5, 1.0, -1.0, 1.0),cmap=cm.Greys_r)
	plt.title('Mandelbrot Set')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.show() 
