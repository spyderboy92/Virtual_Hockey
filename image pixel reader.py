import cv2
import colorsys
im=cv2.imread('pict.jpg')
cv2.imshow('Display',im)

def my_mouse_callback(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDBLCLK:		# here event is left mouse button double-clicked
		print x,y
		print im[x][y]
		j=im[x][y]
		k=colorsys.rgb_to_hsv(j[2]/255.,j[1]/255.,j[0]/255.0)
		x=k[0]
		x=x*360
		y=k[1]*100
		z=k[2]*100
		print x
		print y
		print z
		
cv2.setMouseCallback("Display",my_mouse_callback,im)	#binds the screen,function and image

cv2.waitKey(0)
cv2.destroyAllWindows()
