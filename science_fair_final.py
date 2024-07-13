import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure
import time
#Variables
ang1 = 30
ang2 = 45
ang3 = 60
ang4 = 75
finalDeltaY = 0
finalVY = 0
times = 0
deltaT = 0
vX = 0
initVY = 0
yPos = 0
deltaX = 0
initY = 0 
a = 0
instantVY = 0
xComponent = 0
yComponent = 0
g = -9.81
vectorMag = 0
vectorAng = 0
dt = 0.005
global set
set = 0
valuesList = []
scale = 0
ballSize = 0
sameV = 0
sameDX = 0
sameDY = 0
sameDT = 0
choice = 0
totalThing = 0
thing1 = 0
thing2 = 0
thing3 = 0
thing4 = 0
vx01, vy01 = 0,0
vx02, vy02 = 0,0
vx03, vy03 = 0,0
vx04, vy04 = 0,0
v01 = 0
v02 = 0
v03 = 0
v04 = 0
deltaT1 = 0
deltaX1 = 0
deltaT2 = 0
deltaX2 = 0
deltaT3 = 0
deltaX3 = 0
deltaT4 = 0
deltaX4 = 0
varList = []
varHave = []
varNeeded = []
componentsList = []
operationList = []
numVec = 0
finalVec = []
currentI = 0
currentJ = 0
operationI = 0
operationJ = 0
tickFreq = 0

#functions
def errorCheck(var):
	if len(var) >= 3:
		if var.isnumeric():
			return float(var)
		if var[0].isnumeric():
			for x in range(len(var)):
				if x <= (len(var)-2) and x > 0:
					if var[x-1].isnumeric() and var[x] == "." and var[x+1].isnumeric():
						return float(var)
						break
		else:
			return var()
	elif len(var) <= 2:
		if var.isnumeric():
			return float(var)
		else:
			return var
def errorCheck2(var):
	if len(var) >= 3:
		if var.isnumeric() or (var[0] == "-" and var[1:].isnumeric()):
			return float(var)
		elif var[0].isnumeric() or var[1].isnumeric():
			for x in range(len(var)):
				if x <= (len(var)-2) and x > 0:
					if var[x-1].isnumeric() and var[x] == "." and var[x+1].isnumeric():
						if var[0].isnumeric or (var[0] == "-" and var[1].isnumeric()):
							return float(var)
							break
		else:
			return var
	elif len(var) <= 2:
		if var.isnumeric() or (var[0] == "-" and var[1:].isnumeric()):
			return float(var)
		else:
			return var
def errorCheck3(var):
	if len(var) >= 3:
		if var.isnumeric():
			return float(var)
		elif var[0].isnumeric():
			for x in range(len(var)):
				if x <= (len(var)-2) and x > 0:
					if var[x-1].isnumeric() and var[x] == "." and var[x+1].isnumeric():
						return float(var)
						break
		else:
			return var()
	elif len(var) <= 2:
		if var.isnumeric():
			return float(var)
		else:
			return var
def errorCheck4(var):
	if len(var) >= 3:
		if var.isnumeric():
			return float(var)
		if var[0].isnumeric():
			for x in range(len(var)):
				if x <= (len(var)-2) and x > 0:
					if var[x-1].isnumeric() and var[x] == "." and var[x+1].isnumeric():
						return float(var)
						break
		else:
			return var()
	elif len(var) == 2:
		if var.isnumeric():
			return float(var)
		else:
			return var
	elif len(var) == 1:
		if var.isnumeric():
			return float(var)
		elif var == "g":
			return var
		else:
			return var	
def components(mag, ang):
	radAng = numpy.deg2rad(ang)
	componentsList = []
	xComponent = mag*numpy.cos(radAng)
	yComponent = mag*numpy.sin(radAng)
	componentsList.append(xComponent)
	componentsList.append(yComponent)
	return componentsList

def vector(x, y):
	vectorInfo = []
	num = x**2 + y**2
	mag = numpy.sqrt(num)
	ang = numpy.rad2deg(numpy.arctan((y/x)))
	vectorInfo.append(mag)
	vectorInfo.append(ang)
	return vectorInfo

def balls4(sameV, sameDX, sameDY):
	vx01, vy01 = 0,0
	vx02, vy02 = 0,0
	vx03, vy03 = 0,0
	vx04, vy04 = 0,0
	v01 = 0
	v02 = 0
	v03 = 0
	v04 = 0
	deltaT1 = 0
	deltaX1 = 0
	deltaT2 = 0
	deltaX2 = 0
	deltaT3 = 0
	deltaX3 = 0
	deltaT4 = 0
	deltaX4 = 0
	#Meth
	if sameV == 1:
		components30 = components(vectorMag, ang1)
		components45 = components(vectorMag, ang2)
		components60 = components(vectorMag, ang3)
		components75 = components(vectorMag, ang4)
		print(components30, components45, components60, components75)
		vx01, vy01 = components30[0], components30[1]
		vx02, vy02 = components45[0], components45[1]
		vx03, vy03 = components60[0], components60[1]
		vx04, vy04 = components75[0], components75[1]
		sameV = 0
	
	if sameDX == 1:
		v01 = numpy.sqrt((9.81*finalVX)/numpy.sin(2* numpy.deg2rad(ang1)))
		v02 = numpy.sqrt((9.81*finalVX)/numpy.sin(2* numpy.deg2rad(ang2)))
		v03 = numpy.sqrt((9.81*finalVX)/numpy.sin(2* numpy.deg2rad(ang3)))
		v04 = numpy.sqrt((9.81*finalVX)/numpy.sin(2* numpy.deg2rad(ang4)))
		components30 = components(v01, ang1)
		components45 = components(v02, ang2)
		components60 = components(v03, ang3)
		components75 = components(v04, ang4)
		print(components30, components45, components60, components75)
		vx01, vy01 = components30[0], components30[1]
		vx02, vy02 = components45[0], components45[1]
		vx03, vy03 = components60[0], components60[1]
		vx04, vy04 = components75[0], components75[1]
		sameDX = 0
	
	if sameDY == 1:
		vy01 = numpy.sqrt(2*9.81*maxY)
		vx01 = vy01/(numpy.tan(numpy.deg2rad(ang1)))
		vy02 = numpy.sqrt(2*9.81*maxY)
		vx02 = vy02/(numpy.tan(numpy.deg2rad(ang2)))
		vy03 = numpy.sqrt(2*9.81*maxY)
		vx03 = vy03/(numpy.tan(numpy.deg2rad(ang3)))
		vy04 = numpy.sqrt(2*9.81*maxY)
		vx04 = vy04/(numpy.tan(numpy.deg2rad(ang4)))
		sameDY = 0
		
	deltaT1 = (2*vy01)/9.81
	deltaX1 = vx01*deltaT1
	deltaT2 = (2*vy02)/9.81
	deltaX2 = vx02*deltaT2
	deltaT3 = (2*vy03)/9.81
	deltaX3 = vx03*deltaT3
	deltaT4 = (2*vy04)/9.81
	deltaX4 = vx04*deltaT4
	print(deltaX1)
	print(deltaX2)
	print(deltaX3)
	print(deltaX4)
	
	# Acceleration due to gravity, m.s-2.
	gr = 9.81
	# The maximum x-range of ball's trajectory to plot.
	# The time step for the animation.
	dt = 0
	count = 0
	t = 0
	# Initial position and velocity vectors.
	x0, y0 = 0, 0
	def get_pos(t=0):
		t1 = 0 
		t2 = 0
		t3 = 0
		t4 = 0
		thing1 = 0
		thing2 = 0
		thing3 = 0
		thing4= 0
		totalThing = 0
		count = 0
		dt = 0
		"""A generator yielding the ball's position at time t."""
		x1, y1, x2, y2, x3, y3, x4, y4, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4 = x0, y0, x0, y0, x0, y0, x0, y0, vx01, vy01, vx02, vy02, vx03, vy03, vx04, vy04
		while totalThing == 0:
			t += dt
			if thing1 == 0:
				x1 += vx1 * dt
				y1 += vy1 * dt
				vy1 -= gr * dt
				t1 = t
				velocity1 = numpy.sqrt((vy1**2)+(vx01**2))
				if y1 <= 0 and count != 0:
					y1 = 0
					x1 = deltaX1
					thing1 = 1
					
			if thing2 == 0:
				x2 += vx2 * dt
				y2 += vy2 * dt
				vy2 -= gr * dt
				t2 = t
				velocity2 = numpy.sqrt((vy2**2)+(vx02**2))
				if y2 <= 0 and count != 0:
					y2 = 0
					x2 = deltaX2
					thing2 = 1
					
			if thing3 == 0:
				x3 += vx3 * dt
				y3 += vy3 * dt
				vy3 -= gr * dt
				t3 = t
				velocity3 = numpy.sqrt((vy3**2)+(vx03**2))
				if y3 <= 0 and count != 0:
					y3 = 0
					x3 = deltaX3
					thing3 = 1
					
			if thing4 == 0:
				x4 += vx4 * dt
				y4 += vy4 * dt
				vy4 -= gr * dt
				t4 = t
				velocity4 = numpy.sqrt((vy4**2)+(vx04**2))
				if y4 <= 0 and count != 0:
					y4 = 0
					x4 = deltaX4
					thing4 = 1
	
			if thing1 == 1 and thing2 == 2 and thing3 == 3 and thing4 == 4:
				totalThing = 1
			yield x1, y1, x2, y2, x3, y3, x4, y4, velocity1, velocity2, velocity3, velocity4, t1, t2, t3, t4
			count += 1
			if count == 1:
				dt = 0.01
	
	def init():
		"""Initialize the animation figure."""
		ax.set_xlim(0, 125)
		ax.set_ylim(0, 100)
		ax.set_xlabel('$x$ /m')
		ax.set_ylabel('$y$ /m')
		line1.set_data(xdata1, ydata1)
		line2.set_data(xdata2, ydata2)
		line3.set_data(xdata3, ydata3)
		line4.set_data(xdata4, ydata4)
		ball1.set_center((x0, y0))
		ball2.set_center((x0, y0))
		ball3.set_center((x0, y0))
		ball4.set_center((x0, y0))
		ang1_text.set_text('30°')
		ang1_text.set_position((x0, y0))
		ang2_text.set_text('45°')
		ang2_text.set_position((x0, y0))
		ang3_text.set_text('60°')
		ang3_text.set_position((x0, y0))
		ang4_text.set_text('75°')
		ang4_text.set_position((x0, y0))
		velocityText1.set_text(f'Velocity: {0: .2f} m/s')
		velocityText2.set_text(f'Velocity: {0: .2f} m/s')
		velocityText3.set_text(f'Velocity: {0: .2f} m/s')
		velocityText4.set_text(f'Velocity: {0: .2f} m/s')
		heightText1.set_text(f'Height: {0: .1f} m')
		heightText2.set_text(f'Height: {0: .1f} m')
		heightText3.set_text(f'Height: {0: .1f} m')
		heightText4.set_text(f'Height: {0: .1f} m')
		timeText1.set_text(f'Elapsed Time: {0: .1f} s')
		timeText2.set_text(f'Elapsed Time: {0: .1f} s')
		timeText3.set_text(f'Elapsed Time: {0: .1f} s')
		timeText4.set_text(f'Elapsed Time: {0: .1f} s')
		rangeText1.set_text(f'Range: {0: .1f} m')
		rangeText2.set_text(f'Range: {0: .1f} m')
		rangeText3.set_text(f'Range: {0: .1f} m')
		rangeText4.set_text(f'Range: {0: .1f} m')
		return line1, line2, line3, line4, ball1, ball2, ball3, ball4, ang1_text, ang2_text, ang3_text, ang4_text, velocityText1, velocityText2, velocityText3, velocityText4, heightText1, heightText2, heightText3, heightText4, timeText1, timeText2, timeText3, timeText4, rangeText1, rangeText2, rangeText3, rangeText4
	
	def animate(pos):
		"""For each frame, advance the animation to the new position, pos."""
		x1, y1, x2, y2, x3, y3, x4, y4, velocity1, velocity2, velocity3, velocity4, t1, t2, t3, t4 = pos
		xdata1.append(x1)
		ydata1.append(y1)
		xdata2.append(x2)
		ydata2.append(y2)
		xdata3.append(x3)
		ydata3.append(y3)
		xdata4.append(x4)
		ydata4.append(y4)
		line1.set_data(xdata1, ydata1)
		line2.set_data(xdata2, ydata2)
		line3.set_data(xdata3, ydata3)
		line4.set_data(xdata4, ydata4)
		ball1.set_center((x1, y1))
		ball2.set_center((x2, y2))
		ball3.set_center((x3, y3))
		ball4.set_center((x4, y4))
		ang1_text.set_position((x1, y1))
		ang2_text.set_position((x2, y2))
		ang3_text.set_position((x3, y3))
		ang4_text.set_position((x4, y4))
		velocityText1.set_text(f'Velocity: {velocity1: .1f} m/s')
		velocityText2.set_text(f'Velocity: {velocity2: .1f} m/s')
		velocityText3.set_text(f'Velocity: {velocity3: .1f} m/s')
		velocityText4.set_text(f'Velocity: {velocity4: .1f} m/s')
		heightText1.set_text(f'Height: {y1: .1f} m')
		heightText2.set_text(f'Height: {y2: .1f} m')
		heightText3.set_text(f'Height: {y3: .1f} m')
		heightText4.set_text(f'Height: {y4: .1f} m')
		timeText1.set_text(f'Elapsed Time: {t1: .1f} s')
		timeText2.set_text(f'Elapsed Time: {t2: .1f} s')
		timeText3.set_text(f'Elapsed Time: {t3: .1f} s')
		timeText4.set_text(f'Elapsed Time: {t4: .1f} s')
		rangeText1.set_text(f'Range: {x1: .1f} m')
		rangeText2.set_text(f'Range: {x2: .1f} m')
		rangeText3.set_text(f'Range: {x3: .1f} m')
		rangeText4.set_text(f'Range: {x4: .1f} m')
		return line1, line2, line3, line4, ball1, ball2, ball3, ball4, ang1_text, ang2_text, ang3_text, ang4_text, velocityText1, velocityText2, velocityText3, velocityText4, heightText1, heightText2, heightText3, heightText4, timeText1, timeText2, timeText3, timeText4, rangeText1, rangeText2, rangeText3, rangeText4
	
	# Set up a new Figure, with equal aspect ratio so the ball appears round.
	fig, ax = plt.subplots()
	ax.set_aspect('equal')
	
	# These are the objects we need to keep track of.
	line1, = ax.plot([], [], lw=2)
	line2, = ax.plot([], [], lw=2)
	line3, = ax.plot([], [], lw=2)
	line4, = ax.plot([], [], lw=2)
	ball1 = plt.Circle((x0, y0), 0.5)
	ball2 = plt.Circle((x0, y0), 0.5, color = 'tab:orange')
	ball3 = plt.Circle((x0, y0), 0.5, color = 'g')
	ball4 = plt.Circle((x0, y0), 0.5, color = 'r')
	ax.add_patch(ball1)
	ax.add_patch(ball2)
	ax.add_patch(ball3)
	ax.add_patch(ball4)
	ang1_text = ax.text(x0, y0, '30°', color = 'b')
	ang2_text = ax.text(x0, y0, '45°', color = 'tab:orange')
	ang3_text = ax.text(x0, y0, '60°', color = 'g')
	ang4_text = ax.text(x0, y0, '75°', color = 'r')
	text30 = ax.text(12, 95, '30°', color = 'b')
	text45 = ax.text(44, 95, '45°', color = 'tab:orange')
	text60 = ax.text(76, 95, '60°', color = 'g')
	text75 = ax.text(108, 95, '75°', color = 'r')
	velocityText1 = ax.text(0.1, 90, f'Velocity: {0: .1f} m/s', color = 'b', fontsize = 7.5)
	velocityText2 = ax.text(32.1, 90, f'Velocity: {0: .1f} m/s', color = 'tab:orange', fontsize = 7.5)
	velocityText3 = ax.text(64.1, 90, f'Velocity: {0: .1f} m/s', color = 'g', fontsize = 7.5)
	velocityText4 = ax.text(96.1, 90, f'Velocity: {0: .1f} m/s', color = 'r', fontsize = 7.5)
	heightText1 = ax.text(0.1, 87, f'Height: {0: .1f} m', color = 'b', fontsize = 7.5)
	heightText2 = ax.text(32.1, 87, f'Height: {0: .1f} m', color = 'tab:orange', fontsize = 7.5)
	heightText3 = ax.text(64.1, 87, f'Height: {0: .1f} m', color = 'g', fontsize = 7.5)
	heightText4 = ax.text(96.1, 87, f'Height: {0: .1f} m', color = 'r', fontsize = 7.5)
	timeText1 = ax.text(0.1, 84, f'Elapsed Time: {0: .1f} s', color = 'b', fontsize = 7.5)
	timeText2 = ax.text(32.1, 84, f'Elapsed Time: {0: .1f} s', color = 'tab:orange', fontsize = 7.5)
	timeText3 = ax.text(64.1, 84, f'Elapsed Time: {0: .1f} s', color = 'g', fontsize = 7.5)
	timeText4 = ax.text(96.1, 84, f'Elapsed Time: {0: .1f} s', color = 'r', fontsize = 7.5)
	rangeText1 = ax.text(0.1, 81, f'Range: {0: .1f} m', color = 'b', fontsize = 7.5)
	rangeText2 = ax.text(32.1, 81, f'Range: {0: .1f} m', color = 'tab:orange', fontsize = 7.5)
	rangeText3 = ax.text(64.1, 81, f'Range: {0: .1f} m', color = 'g', fontsize = 7.5)
	rangeText4 = ax.text(96.1, 81, f'Range: {0: .1f} m', color = 'r', fontsize = 7.5)
	xdata1, xdata2, xdata3, xdata4, ydata1, ydata2, ydata3, ydata4 = [], [], [], [], [], [], [], []
	interval = 100*dt
	
	def on_press(event):
		if event.key.isspace():
			if ani.running:
				ani.resume()
			else:
				ani.pause()
			ani.running ^= True
	fig.canvas.mpl_connect('key_press_event', on_press)
	
	ani = animation.FuncAnimation(fig, animate, get_pos, blit=True,
													interval=interval, repeat=False, init_func=init)
	ani.running = True
	plt.show()
	
def regProjMotion():
	componentsList = components(vectorMag, vectorAng)
	vX = componentsList[0]
	initVY = componentsList[1]
	
	#Meth
	finalDeltaY = 0 - initY
	maxY = (((-(initVY**2))/(2*a)) + initY)
	print(maxY)
	
	finalVY= -(numpy.sqrt((initVY**2 + 2*a*finalDeltaY)))
	print(finalVY)
	final_velocity = numpy.sqrt((finalVY*finalVY)+(vX*vX))
	totalT = (finalVY-initVY)/a
	print(totalT)
	finalX = (totalT*vX)
	print(finalX)
	
	#Variables/0.0001 sec
	
	if scale == '1':
		xMax = 15
		yMax = 15
		yMin = -5
		tickFreq = 1
		ballSize = 0.2
	elif scale == '2':
		xMax = 100
		yMax = 100
		yMin = -30
		tickFreq = 10
		ballSize = 1.5
	elif scale == '3':
		xMax = 250
		yMax = 250
		yMin = -50
		tickFreq = 25
		ballSize = 3
	
	# Acceleration due to gravity, m.s-2.
	gr = -a
	# The maximum x-range of ball's trajectory to plot.
	XMAX = finalX
	# The time step for the animation.
	dt = 0
	count = 0
	t = 0
	# Initial position and velocity vectors.
	x0, y0 = 0, initY
	vx0, vy0 = vX, initVY
	initialVelocity = numpy.sqrt((vy0**2)+(vx0**2))
	def get_pos(t=0):
		count = 0
		dt = 0
		vxPos = 0
		vyPos = 0
		"""A generator yielding the ball's position at time t."""
		x, y, vy, vx = x0, y0, vy0, vx0
		while y >= 0:
			t += dt
			x += vx0 * dt
			y += vy * dt
			vy -= gr * dt
			ang = numpy.rad2deg(numpy.arctan(vy/vx))
			velocity = numpy.sqrt((vy**2)+(vx**2))
			vxPos = x + vx
			vyPos = y + vy
			
			if y < 0:
				y = -0.000000001
				velocity = final_velocity
				t = totalT
			yield x, y, velocity, t, ang, vxPos, vyPos, vx, vy, gr
			count += 1
			if count == 1:
				dt = 0.01
	
	def init():
		"""Initialize the animation figure."""
		ax1.set_xlim(0, xMax)
		ax1.set_ylim(yMin, yMax)
		ax1.set_xlabel('Δx (m)')
		ax1.set_ylabel('Δy (m)')
		ax1.set_title("Trajectory of the Projectile")
		length1StartX, length1EndX = ax1.get_xlim()
		ax1.xaxis.set_ticks(numpy.arange(length1StartX, length1EndX, tickFreq))
		length1StartY, length1EndY = ax1.get_ylim()
		ax1.yaxis.set_ticks(numpy.arange(length1StartY, length1EndY, tickFreq))
		ax2.set_xlim(0,15)
		ax2.set_ylim(-40,40)
		ax2.set_xlabel('time (s)')
		ax2.set_ylabel('velocity (m/s)')
		ax2.set_title("Velocity as a Function of Time")
		ax2.yaxis.set_ticks(numpy.arange(-40, 40, 5))
		ax3.set_xlim(0,15)
		ax3.set_ylim(-20,20)
		ax3.xaxis.set_ticks(numpy.arange(0, 15, 2))
		ax3.yaxis.set_ticks(numpy.arange(-20, 20, 2.5))
		ax3.set_xlabel('time (s)')
		ax3.set_ylabel('acceleration (m/s^2)')
		ax3.set_title("Acceleration as a Function of Time")
		mainLine.set_data(xdata, ydata)
		velocityLineX.set_data(tdata, velocityXData)
		velocityLineY.set_data(tdata, velocityYData)
		aLine.set_data(tdata, adata)
		ball.set_center((x0, y0))
		vArrow = plt.Arrow(x0,y0,x0,y0,width = ballSize, color = 'tab:orange')
		addvArrow = ax1.add_patch(vArrow)
		addvArrow.remove()
		addvArrow = ax1.add_patch(vArrow)
		vxArrow = plt.Arrow(x0,y0,x0,y0,width = ballSize, color = 'g')
		addvxArrow = ax1.add_patch(vxArrow)
		addvxArrow.remove()
		addvxArrow = ax1.add_patch(vxArrow)
		vyArrow = plt.Arrow(x0,y0,x0,y0,width = ballSize, color = 'r')
		addvyArrow = ax1.add_patch(vyArrow)
		addvyArrow.remove()
		addvyArrow = ax1.add_patch(vyArrow)
		height_text.set_text(f'Height: {y0:.2f} m')
		range_text.set_text(f'Range: {x0: .2f} m')
		velocity = initialVelocity
		t = 0
		velocity_text.set_text(f'Velocity: {velocity: .2f} m/s')
		time_text.set_text(f'Elapsed Time: {t: .2f} s')
		return mainLine, ball, height_text, velocity_text, time_text, range_text, velocityLineX, velocityLineY, aLine, vArrow, addvArrow, vxArrow, addvxArrow, vyArrow, addvyArrow
	
	def animate(pos):
		"""For each frame, advance the animation to the new position, pos."""
		x, y, velocity, t, ang, vxPos, vyPos, vx, vy, gr = pos
		xdata.append(x)
		ydata.append(y)
		vxdata.append(vxPos)
		vydata.append(vyPos)
		tdata.append(t)
		adata.append(-gr)
		velocityXData.append(vx)
		velocityYData.append(vy)
		mainLine.set_data(xdata, ydata)
		velocityLineX.set_data(tdata, velocityXData)
		velocityLineY.set_data(tdata, velocityYData)
		aLine.set_data(tdata, adata)
		ball.set_center((x, y))
		vArrow = plt.Arrow(x,y,vxPos-x,vyPos-y,width = ballSize, color = 'tab:orange')
		addvArrow = ax1.add_patch(vArrow)
		addvArrow.remove()
		addvArrow = ax1.add_patch(vArrow)
		vxArrow = plt.Arrow(x,y,vxPos-x,0,width = ballSize, color = 'g')
		addvxArrow = ax1.add_patch(vxArrow)
		addvxArrow.remove()
		addvxArrow = ax1.add_patch(vxArrow)
		vyArrow = plt.Arrow(x,y,0,vyPos-y,width = ballSize, color = 'r')
		addvyArrow = ax1.add_patch(vyArrow)
		addvyArrow.remove()
		addvyArrow = ax1.add_patch(vyArrow)
		height_text.set_text(f'Height: {y:.2f} m')
		range_text.set_text(f'Range: {x: .2f} m')
		velocity_text.set_text(f'Velocity: {velocity:.2f} m/s')
		time_text.set_text(f'Elapsed Time: {t: .2f} s')
		return mainLine, ball, height_text, velocity_text, time_text, range_text, velocityLineX, velocityLineY, aLine, vArrow, addvArrow, vxArrow, addvxArrow, vyArrow, addvyArrow
	
	# Set up a new Figure, with equal aspect ratio so the ball appears round.
	fig, (ax1,ax2,ax3) = plt.subplots(1,3, gridspec_kw={'width_ratios': [3, 1.25, 1]})
	fig.set_size_inches(18, 12)
	ax1.set_aspect(1)
	ax2.set_aspect('auto')
	ax3.set_aspect('auto')
	
	# These are the objects we need to keep track of.
	mainLine, = ax1.plot([], [], lw=2)
	ball = plt.Circle((x0, y0), ballSize)
	velocityLineX, = ax2.plot([], [], lw = 2)
	velocityLineY, = ax2.plot([], [], lw = 2)
	aLine, = ax3.plot([], [], lw = 2)
	height_text = ax1.text(xMax*0.65, yMax*0.85, f'Height: {y0:.2f} m')
	velocity_text = ax1.text(xMax*0.65, yMax*0.9, f'Velocity: {initialVelocity: .2f} m/s')
	time_text = ax1.text(xMax*0.65, yMax*0.8, f'Elapsed Time: {t: .2f} s')
	range_text = ax1.text(xMax*0.65, yMax*0.75, f'Range: {x0:.2f} m')
	xComponentText = ax2.text(0,36, "Velocity of the X Component", fontsize = 8, color = "b")
	YComponentText = ax2.text(0,33, "Velocity of the Y Component", fontsize = 8, color = "tab:orange")
	vArrow = plt.Arrow(0,0,0,0, width = ballSize, color = 'tab:orange')
	addvArrow = ax1.add_patch(vArrow)
	vxArrow = plt.Arrow(0,0,0,0, width = ballSize, color = 'g')
	addvxArrow = ax1.add_patch(vxArrow)
	vyArrow = plt.Arrow(0,0,0,0, width = ballSize, color = 'r')
	addvyArrow = ax1.add_patch(vyArrow)
	x0Arrow1 = plt.Arrow(0,0,1000,0, width = ballSize, color = 'k')
	ax1.add_patch(x0Arrow1)
	x0Arrow2 = plt.Arrow(0,0,1000,0, width = 2, color = 'k')
	ax2.add_patch(x0Arrow2)
	x0Arrow3 = plt.Arrow(0,0,1000,0, width = 1, color = 'k')
	ax3.add_patch(x0Arrow3)
	ax1.add_patch(ball)
	xdata, ydata, velocityXData, velocityYData, vxdata, vydata, tdata, adata = [], [], [], [], [], [], [], []
	interval = 100*dt
	
	def on_press(event):
		if event.key.isspace():
			if ani.running:
				ani.resume()
			else:
				ani.pause()
			ani.running ^= True
	fig.canvas.mpl_connect('key_press_event', on_press)
	
	ani = animation.FuncAnimation(fig, animate, get_pos, blit=True,
													interval=interval, repeat=False, init_func=init)
	ani.running = True
	plt.show()

	

def openVar():
	variablesWindow = tk.Tk()
	variablesWindow.geometry('500x500')
	label1 = tk.Label(master = variablesWindow, fg = 'yellow', bg = 'black', width = 15, text = "Magnitude (m/s):")
	label1.place(x=120,y=10)
	magEntry = tk.Entry(master = variablesWindow, fg='black', bg = 'white', width = 20)
	magEntry.place(x=250,y=12)
	label2 = tk.Label(master = variablesWindow, fg = 'yellow', bg = 'black', width = 15, text = "Angle (°):")
	label2.place(x=120,y=50)
	angleEntry = tk.Entry(master = variablesWindow, fg='black', bg = 'white', width = 20)
	angleEntry.place(x=250,y=52)
	label3 = tk.Label(master = variablesWindow, fg = 'yellow', bg = 'black', width = 15, text = "Initial Height (m):")
	label3.place(x=120,y=90)
	heightEntry = tk.Entry(master = variablesWindow, fg='black', bg = 'white', width = 20)
	heightEntry.place(x=250,y=92)
	label4 = tk.Label(master = variablesWindow, fg = 'yellow', bg = 'black', width = 15, text = "Acceleration (m/s²):")
	label4.place(x=120,y=130)
	gravityEntry = tk.Entry(master = variablesWindow, fg='black', bg = 'white', width = 20)
	gravityEntry.place(x=250,y=132)
	label5 = tk.Label(master = variablesWindow, fg = 'yellow', bg = 'black', width = 15, text = "Scale:")
	label5.place(x=120,y=170)
	scaleEntry = tk.Entry(master = variablesWindow, fg='black', bg = 'white', width = 20)
	scaleEntry.place(x=250,y=172)
	label6 = tk.Label(master = variablesWindow, fg = 'yellow', bg = 'black', width = 10, text = "Scales\n1: Small\n2: Medium\n3: Large")
	label6.place(x=200,y=340)
	label7 = tk.Label(master = variablesWindow, fg = 'yellow', bg = 'black', width = 35, text = "For acceleration, g = Earth's gravity (9.81m/s²)")
	label7.place(x=125,y=440)
	def getFields():
		badInput = 'true'
		magEntryVal = magEntry.get()
		magEntryVal = errorCheck3(magEntryVal)
		angEntryVal = angleEntry.get()
		angEntryVal = errorCheck3(angEntryVal)
		heightEntryVal = heightEntry.get()
		heightEntryVal = errorCheck3(heightEntryVal)
		a2 = gravityEntry.get()
		a2 = errorCheck4(a2)
		scaleEntryVal = scaleEntry.get()
		global vectorMag
		global vectorAng
		global initY
		global a
		global scale
		if isinstance(magEntryVal, float):
				vectorMag = magEntryVal
		else:
			badInput = 'false'
		if isinstance(angEntryVal, float):
				vectorAng = angEntryVal
		else:
			badInput = 'false'
		if isinstance(heightEntryVal, float):
				initY = heightEntryVal
		else:
			badInput = 'false'
		if isinstance(a2, float) or a2 == "g":
			if a2 == "g":
				a = -9.81
			else:
				a = a2
				if a > 0:
					a = -a
				elif a < 0:
					a = a
		else: 
			badInput = 'false'
		if scaleEntryVal == '1' or scaleEntryVal == '2' or scaleEntryVal == '3':
			scale = scaleEntryVal
		else: 
			badInput = 'false'
		if badInput == 'false':
			error_label = tk.Label(master = variablesWindow, height = 2, width = 30, foreground = 'red', background = 'black', text = 'ERROR: One or more values are incorrect')
			error_label.place(x=135, y=300)
		else: 
			regProjMotion()
			

	start_button = tk.Button(master = variablesWindow, command = getFields, height = 2, width = 10, text = "Start")
	start_button.place(x=200, y =250)
def instructions():
	instructionsPage = tk.Tk()
	instructionsPage.geometry('500x500')
	label1 = tk.Label(master = instructionsPage, text= 'Welcome to our physics simulator!', foreground = 'black', width = 25, height = 6)
	label1.pack()
	label2 = tk.Label(font = ('bold'), master = instructionsPage, text= 'Parameters Comparison', foreground = 'black', width = 50, height = 2)
	label2.pack()
	label3 = tk.Label(master = instructionsPage, text= 'This feature allows users to view how different parameters \naffect the trajectory of an object', foreground = 'black', width = 50, height = 4)
	label3.pack()
	label4 = tk.Label(font = ('bold'), master = instructionsPage, text= 'Visualizer', foreground = 'black', width = 50, height = 2)
	label4.pack()
	label5 = tk.Label(master = instructionsPage, text= 'This feature allows users to input their own parameters \nand see how they affect the motion of the projectile', foreground = 'black', width = 50, height = 4)
	label5.pack()
	label6 = tk.Label(font = ('bold'), master = instructionsPage, text= 'Vector Visualizer', foreground = 'black', width = 50, height = 2)
	label6.pack()
	label7 = tk.Label(master = instructionsPage, text= 'This feature allows users to visualize\n vector operations and their resultants', foreground = 'black', width = 50, height = 4)
	label7.pack()
def velocityBalls():
	global sameV
	global vectorMag
	sameV = 1
	vectorMag = 30
	balls4(sameV, 0, 0)
def rangeBalls():
	global sameDX
	global finalVX
	sameDX = 1
	finalVX = 50
	balls4(0, sameDX, 0)
def heightBalls():
	global sameDY
	global maxY
	sameDY = 1
	maxY = 10
	balls4(0, 0, sameDY)
def fourBallsMenu():
	ballsMenu = tk.Tk()
	ballsMenu.geometry('500x500')
	ballsLabel = tk.Label(master = ballsMenu, text = 'Choose a parameter', font=('bold'),foreground = 'black', width = 25, height = 5)
	ballsLabel.pack()
	velocity_button = tk.Button(master = ballsMenu, command = velocityBalls, height = 2, width = 12, text = "Same Velocity")
	velocity_button.place(x=200, y= 100)
	range_button = tk.Button(master = ballsMenu, command = rangeBalls, height = 2, width = 10, text = "Same Range")
	range_button.place(x=205, y= 200)
	height_button = tk.Button(master = ballsMenu, command = heightBalls, height = 2, width = 15, text = "Same Max Height")
	height_button.place(x=190, y= 300)
def vectorCalc():
	fig, ax = plt.subplots(1,1)
	ax.set_xlim(-50, 50)
	ax.set_ylim(-50,50)
	finalVec.append(componentsList[0])
	finalVec.append(componentsList[1])
	for x in range(0,numVec*2, 2):
		print(x)
		currentI = finalVec[0]
		currentJ = finalVec[1]
		if x == 0:
			operationI = componentsList[0]
			operationJ = componentsList[1]
			arrow = plt.Arrow(0,0,componentsList[int(x)],componentsList[int(x+1)],width = 5)
		elif operationList[int(x/2-1)] == '+':
			operationI = currentI + componentsList[int(x)]
			operationJ = currentJ + componentsList[int(x+1)]
			arrow = plt.Arrow(currentI,currentJ,componentsList[int(x)],componentsList[int(x+1)],width = 5)
		elif operationList[int(x/2-1)] == '-':
			operationI = currentI - componentsList[int(x)]
			operationJ = currentJ - componentsList[int(x+1)]
			arrow = plt.Arrow(currentI,currentJ,-componentsList[int(x)],-componentsList[int(x+1)],width = 5)
		finalVec.clear()
		finalVec.append(operationI)
		finalVec.append(operationJ)
		ax.add_patch(arrow)
	print(finalVec)
	arrow = plt.Arrow(0,0,finalVec[0],finalVec[1],width = 5, color = "r")
	ax.add_patch(arrow)
	plt.show()
	
def magVectors():
	vectorMenu2 = tk.Tk()
	vectorMenu2.geometry('500x500')
	vectorLabel2 = tk.Label(master = vectorMenu2, text = 'How many vectors would you like to add/subtract?',font=('bold'), width = 50, height = 5, fg = 'black')
	vectorLabel2.pack()
	def two_vectors():
		vectorMenu3 = tk.Tk()
		vectorMenu3.geometry('500x500')
		vectorLabel3 = tk.Label(master = vectorMenu3, text = 'Magnitudes', width = 20, height = 5, fg = 'black')
		vectorLabel3.place(x=115, y=100)
		vectorLabel4 = tk.Label(master = vectorMenu3, text = 'Directions', width = 20, height = 5, fg = 'black')
		vectorLabel4.place(x=235, y=100)
		componentLabel1 = tk.Label(master = vectorMenu3, text = '+ or -', width = 25, height = 5, fg = 'black')
		componentLabel1.place(x=150, y=240)
		mag1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag1Entry.place(x=120,y=180)
		mag2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag2Entry.place(x=120,y=210)
		dir1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir1Entry.place(x=250,y=180)
		dir2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir2Entry.place(x=250,y=210)
		comp1Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp1Entry.place(x=180,y=300)
		def checker2():
			global componentsList
			global numVec
			global operationList
			mag1 = mag1Entry.get()
			mag1 = errorCheck(mag1)
			mag2 = mag2Entry.get()
			mag2 = errorCheck(mag2)
			dir1 = dir1Entry.get()
			dir1 = errorCheck(dir1)
			dir2 = dir2Entry.get()
			dir2 = errorCheck(dir2)
			comp1 = comp1Entry.get()
			comp1 = errorCheck(comp1)
			if isinstance(mag1, float) and isinstance(mag2,float) and isinstance(dir1,float) and isinstance(dir2, float) and comp1 == '+' or comp1 == '-':
				componentsList = []
				operationList = []
				xComponent1 = mag1*numpy.cos(numpy.deg2rad(dir1))
				yComponent1 = mag1*numpy.sin(numpy.deg2rad(dir1))
				xComponent2 = mag2*numpy.cos(numpy.deg2rad(dir2))
				yComponent2 = mag2*numpy.sin(numpy.deg2rad(dir2))
				componentsList.append(xComponent1)
				componentsList.append(yComponent1)
				componentsList.append(xComponent2)
				componentsList.append(yComponent2)
				operationList.append(comp1)
				numVec = 2
				vectorCalc()
			else: 
				error_label = tk.Label(master = vectorMenu3, height = 2, width = 30, foreground = 'red', background = 'black', text = 'ERROR: One or more values are incorrect')
				error_label.place(x=135, y=230)
		start1 = tk.Button(master = vectorMenu3, command = checker2, height = 2, width = 10, text = 'START')
		start1.place(x=200,y=350)
	def three_vectors():
		vectorMenu3 = tk.Tk()
		vectorMenu3.geometry('500x500')
		vectorLabel3 = tk.Label(master = vectorMenu3, text = 'Magnitudes', width = 20, height = 5, fg = 'black')
		vectorLabel3.place(x=115, y=50)
		vectorLabel4 = tk.Label(master = vectorMenu3, text = 'Directions', width = 20, height = 5, fg = 'black')
		vectorLabel4.place(x=235, y=50)
		componentLabel1 = tk.Label(master = vectorMenu3, text = '+ or - for operations (in order)', width = 25, height = 5, fg = 'black')
		componentLabel1.place(x=150, y=250)
		mag1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag1Entry.place(x=120,y=130)
		mag2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag2Entry.place(x=120,y=160)
		mag3Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag3Entry.place(x=120,y=190)
		dir1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir1Entry.place(x=250,y=130)
		dir2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir2Entry.place(x=250,y=160)
		dir3Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir3Entry.place(x=250,y=190)
		comp1Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp1Entry.place(x=180,y=310)
		comp2Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp2Entry.place(x=180,y=350)
		def checker3():
			global componentsList
			global numVec
			global operationList
			mag1 = mag1Entry.get()
			mag1 = errorCheck(mag1)
			mag2 = mag2Entry.get()
			mag2 = errorCheck(mag2)
			mag3 = mag3Entry.get()
			mag3 = errorCheck(mag3)
			dir1 = dir1Entry.get()
			dir1 = errorCheck(dir1)
			dir2 = dir2Entry.get()
			dir2 = errorCheck(dir2)
			dir3 = dir3Entry.get()
			dir3 = errorCheck(dir3)
			comp1 = comp1Entry.get()
			comp1 = errorCheck(comp1)
			comp2 = comp2Entry.get()
			comp2 = errorCheck(comp2)
			if isinstance(mag1, float) and isinstance(mag2,float) and isinstance(mag3, float) and isinstance(dir1,float) and isinstance(dir2, float) and isinstance(dir3, float) and comp1 == '+' or comp1 == '-' and comp2 == '+' or comp2 == '+':
				componentsList = []
				operationList = []
				xComponent1 = mag1*numpy.cos(numpy.deg2rad(dir1))
				yComponent1 = mag1*numpy.sin(numpy.deg2rad(dir1))
				xComponent2 = mag2*numpy.cos(numpy.deg2rad(dir2))
				yComponent2 = mag2*numpy.sin(numpy.deg2rad(dir2))
				xComponent3 = mag3*numpy.cos(numpy.deg2rad(dir3))
				yComponent3 = mag3*numpy.sin(numpy.deg2rad(dir3))
				componentsList.append(xComponent1)
				componentsList.append(yComponent1)
				componentsList.append(xComponent2)
				componentsList.append(yComponent2)
				componentsList.append(xComponent3)
				componentsList.append(yComponent3)
				print(componentsList)
				operationList.append(comp1)
				operationList.append(comp2)
				numVec = 3
				vectorCalc()
			else: 
				error_label = tk.Label(master = vectorMenu3, height = 2, width = 30, foreground = 'red', background = 'black', text = 'ERROR: One or more values are incorrect')
				error_label.place(x=135, y=410)
		start1 = tk.Button(master = vectorMenu3, command = checker3, height = 2, width = 10, text = 'START')
		start1.place(x=200,y=450)
	def four_vectors():
		vectorMenu3 = tk.Tk()
		vectorMenu3.geometry('500x500')
		vectorLabel3 = tk.Label(master = vectorMenu3, text = 'Magnitudes', width = 20, height = 5, fg = 'black')
		vectorLabel3.place(x=115, y=20)
		vectorLabel4 = tk.Label(master = vectorMenu3, text = 'Directions', width = 20, height = 5, fg = 'black')
		vectorLabel4.place(x=235, y=20)
		componentLabel1 = tk.Label(master = vectorMenu3, text = '+ or - for operations (in order)', width = 25, height = 5, fg = 'black')
		componentLabel1.place(x=150, y=220)
		mag1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag1Entry.place(x=120,y=100)
		mag2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag2Entry.place(x=120,y=130)
		mag3Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag3Entry.place(x=120,y=160)
		mag4Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag4Entry.place(x=120,y=190)
		dir1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir1Entry.place(x=250,y=100)
		dir2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir2Entry.place(x=250,y=130)
		dir3Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir3Entry.place(x=250,y=160)
		dir4Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir4Entry.place(x=250,y=190)
		comp1Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp1Entry.place(x=180,y=280)
		comp2Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp2Entry.place(x=180,y=320)
		comp3Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp3Entry.place(x=180,y=360)
		def checker4():
			global componentsList
			global numVec
			global operationList
			mag1 = mag1Entry.get()
			mag1 = errorCheck(mag1)
			mag2 = mag2Entry.get()
			mag2 = errorCheck(mag2)
			mag3 = mag3Entry.get()
			mag3 = errorCheck(mag3)
			mag4 = mag4Entry.get()
			mag4 = errorCheck(mag4)
			dir1 = dir1Entry.get()
			dir1 = errorCheck(dir1)
			dir2 = dir2Entry.get()
			dir2 = errorCheck(dir2)
			dir3 = dir3Entry.get()
			dir3 = errorCheck(dir3)
			dir4 = dir4Entry.get()
			dir4 = errorCheck(dir4)
			comp1 = comp1Entry.get()
			comp1 = errorCheck(comp1)
			comp2 = comp2Entry.get()
			comp2 = errorCheck(comp2)
			comp3 = comp3Entry.get()
			comp3 = errorCheck(comp3)
			if isinstance(mag1, float) and isinstance(mag2,float) and isinstance(mag3, float) and isinstance(mag4, float) and isinstance(dir1,float) and isinstance(dir2, float) and isinstance(dir3, float) and isinstance(dir4, float) and comp1 == '+' or comp1 == '-' and comp2 == '+' or comp2 == '+' and comp3 == '+' or comp3 == '-':
				componentsList = []
				operationList = []
				xComponent1 = mag1*numpy.cos(numpy.deg2rad(dir1))
				yComponent1 = mag1*numpy.sin(numpy.deg2rad(dir1))
				xComponent2 = mag2*numpy.cos(numpy.deg2rad(dir2))
				yComponent2 = mag2*numpy.sin(numpy.deg2rad(dir2))
				xComponent3 = mag3*numpy.cos(numpy.deg2rad(dir3))
				yComponent3 = mag3*numpy.sin(numpy.deg2rad(dir3))
				xComponent4 = mag4*numpy.cos(numpy.deg2rad(dir4))
				yComponent4 = mag4*numpy.sin(numpy.deg2rad(dir4))
				componentsList.append(xComponent1)
				componentsList.append(yComponent1)
				componentsList.append(xComponent2)
				componentsList.append(yComponent2)
				componentsList.append(xComponent3)
				componentsList.append(yComponent3)
				componentsList.append(xComponent4)
				componentsList.append(yComponent4)
				operationList.append(comp1)
				operationList.append(comp2)
				operationList.append(comp3)
				numVec = 4
				vectorCalc()
			else: 
				error_label = tk.Label(master = vectorMenu3, height = 2, width = 30, foreground = 'red', background = 'black', text = 'ERROR: One or more values are incorrect')
				error_label.place(x=135, y=400)
		start1 = tk.Button(master = vectorMenu3, command = checker4, height = 2, width = 10, text = 'START')
		start1.place(x=200,y=450)
	two_button = tk.Button(master = vectorMenu2, command = two_vectors, height = 2, width = 10, text = '2')
	two_button.place(x=60, y=150)
	
	three_button = tk.Button(master = vectorMenu2, command = three_vectors, height = 2, width = 10, text = '3')
	three_button.place(x=210, y=150)
	four_button = tk.Button(master = vectorMenu2, command = four_vectors, height = 2, width = 10, text = '4')
	four_button.place(x=350, y=150)
	

def compVectors():
	vectorMenu2 = tk.Tk()
	vectorMenu2.geometry('500x500')
	vectorLabel2 = tk.Label(master = vectorMenu2, text = 'How many vectors would you like to add/subtract?', font=('bold'),width = 50, height = 5, fg = 'black')
	vectorLabel2.pack()
	def two_vectors():
		vectorMenu3 = tk.Tk()
		vectorMenu3.geometry('500x500')
		vectorLabel3 = tk.Label(master = vectorMenu3, text = 'X Components', width = 20, height = 5, fg = 'black')
		vectorLabel3.place(x=115, y=100)
		vectorLabel4 = tk.Label(master = vectorMenu3, text = 'Y Components', width = 20, height = 5, fg = 'black')
		vectorLabel4.place(x=235, y=100)
		componentLabel1 = tk.Label(master = vectorMenu3, text = '+ or -', width = 25, height = 5, fg = 'black')
		componentLabel1.place(x=150, y=240)
		mag1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag1Entry.place(x=120,y=180)
		mag2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag2Entry.place(x=120,y=210)
		dir1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir1Entry.place(x=250,y=180)
		dir2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir2Entry.place(x=250,y=210)
		comp1Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp1Entry.place(x=180,y=300)
		def checker2():
			global componentsList
			global numVec
			global operationList
			mag1 = mag1Entry.get()
			mag1 = errorCheck2(mag1)
			mag2 = mag2Entry.get()
			mag2 = errorCheck2(mag2)
			dir1 = dir1Entry.get()
			dir1 = errorCheck2(dir1)
			dir2 = dir2Entry.get()
			dir2 = errorCheck2(dir2)
			comp1 = comp1Entry.get()
			comp1 = errorCheck(comp1)
			if isinstance(mag1, float) and isinstance(mag2,float) and isinstance(dir1,float) and isinstance(dir2, float) and comp1 == '+' or comp1 == '-':
				componentsList = []
				operationList = []
				xComponent1 = mag1
				yComponent1 = dir1
				xComponent2 = mag2
				yComponent2 = dir2
				componentsList.append(xComponent1)
				componentsList.append(yComponent1)
				componentsList.append(xComponent2)
				componentsList.append(yComponent2)
				operationList.append(comp1)
				numVec = 2
				vectorCalc()
			else: 
				error_label = tk.Label(master = vectorMenu3, height = 2, width = 30, foreground = 'red', background = 'black', text = 'ERROR: One or more values are incorrect')
				error_label.place(x=135, y=230)
		start1 = tk.Button(master = vectorMenu3, command = checker2, height = 2, width = 10, text = 'START')
		start1.place(x=200,y=350)
	def three_vectors():
		vectorMenu3 = tk.Tk()
		vectorMenu3.geometry('500x500')
		vectorLabel3 = tk.Label(master = vectorMenu3, text = 'X Components', width = 20, height = 5, fg = 'black')
		vectorLabel3.place(x=115, y=50)
		vectorLabel4 = tk.Label(master = vectorMenu3, text = 'Y Components', width = 20, height = 5, fg = 'black')
		vectorLabel4.place(x=235, y=50)
		componentLabel1 = tk.Label(master = vectorMenu3, text = '+ or - for operations (in order)', width = 25, height = 5, fg = 'black')
		componentLabel1.place(x=150, y=250)
		mag1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag1Entry.place(x=120,y=130)
		mag2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag2Entry.place(x=120,y=160)
		mag3Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag3Entry.place(x=120,y=190)
		dir1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir1Entry.place(x=250,y=130)
		dir2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir2Entry.place(x=250,y=160)
		dir3Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir3Entry.place(x=250,y=190)
		comp1Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp1Entry.place(x=180,y=310)
		comp2Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp2Entry.place(x=180,y=350)
		def checker3():
			global componentsList
			global numVec
			global operationList
			mag1 = mag1Entry.get()
			mag1 = errorCheck2(mag1)
			mag2 = mag2Entry.get()
			mag2 = errorCheck2(mag2)
			mag3 = mag3Entry.get()
			mag3 = errorCheck2(mag3)
			dir1 = dir1Entry.get()
			dir1 = errorCheck2(dir1)
			dir2 = dir2Entry.get()
			dir2 = errorCheck2(dir2)
			dir3 = dir3Entry.get()
			dir3 = errorCheck2(dir3)
			comp1 = comp1Entry.get()
			comp1 = errorCheck(comp1)
			comp2 = comp2Entry.get()
			comp2 = errorCheck(comp2)
			if isinstance(mag1, float) and isinstance(mag2,float) and isinstance(mag3, float) and isinstance(dir1,float) and isinstance(dir2, float) and isinstance(dir3, float) and comp1 == '+' or comp1 == '-' and comp2 == '+' or comp2 == '+':
				componentsList = []
				operationList = []
				xComponent1 = mag1
				yComponent1 = dir1
				xComponent2 = mag2
				yComponent2 = dir2
				xComponent3 = mag3
				yComponent3 = dir3
				componentsList.append(xComponent1)
				componentsList.append(yComponent1)
				componentsList.append(xComponent2)
				componentsList.append(yComponent2)
				componentsList.append(xComponent3)
				componentsList.append(yComponent3)
				print(componentsList)
				operationList.append(comp1)
				operationList.append(comp2)
				numVec = 3
				vectorCalc()
			else: 
				error_label = tk.Label(master = vectorMenu3, height = 2, width = 30, foreground = 'red', background = 'black', text = 'ERROR: One or more values are incorrect')
				error_label.place(x=135, y=410)
		start1 = tk.Button(master = vectorMenu3, command = checker3, height = 2, width = 10, text = 'START')
		start1.place(x=200,y=450)
	def four_vectors():
		vectorMenu3 = tk.Tk()
		vectorMenu3.geometry('500x500')
		vectorLabel3 = tk.Label(master = vectorMenu3, text = 'X Components', width = 20, height = 5, fg = 'black')
		vectorLabel3.place(x=115, y=20)
		vectorLabel4 = tk.Label(master = vectorMenu3, text = 'Y Components', width = 20, height = 5, fg = 'black')
		vectorLabel4.place(x=235, y=20)
		componentLabel1 = tk.Label(master = vectorMenu3, text = '+ or - for operations (in order)', width = 25, height = 5, fg = 'black')
		componentLabel1.place(x=150, y=220)
		mag1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag1Entry.place(x=120,y=100)
		mag2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag2Entry.place(x=120,y=130)
		mag3Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag3Entry.place(x=120,y=160)
		mag4Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		mag4Entry.place(x=120,y=190)
		dir1Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir1Entry.place(x=250,y=100)
		dir2Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir2Entry.place(x=250,y=130)
		dir3Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir3Entry.place(x=250,y=160)
		dir4Entry = tk.Entry(master = vectorMenu3, fg='black', bg = 'white', width = 20)
		dir4Entry.place(x=250,y=190)
		comp1Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp1Entry.place(x=180,y=280)
		comp2Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp2Entry.place(x=180,y=320)
		comp3Entry = tk.Entry(master = vectorMenu3, fg = 'black', bg = 'white', width = 20)
		comp3Entry.place(x=180,y=360)
		def checker4():
			global componentsList
			global numVec
			global operationList
			mag1 = mag1Entry.get()
			mag1 = errorCheck2(mag1)
			mag2 = mag2Entry.get()
			mag2 = errorCheck2(mag2)
			mag3 = mag3Entry.get()
			mag3 = errorCheck2(mag3)
			mag4 = mag4Entry.get()
			mag4 = errorCheck2(mag4)
			dir1 = dir1Entry.get()
			dir1 = errorCheck2(dir1)
			dir2 = dir2Entry.get()
			dir2 = errorCheck2(dir2)
			dir3 = dir3Entry.get()
			dir3 = errorCheck2(dir3)
			dir4 = dir4Entry.get()
			dir4 = errorCheck2(dir4)
			comp1 = comp1Entry.get()
			comp1 = errorCheck(comp1)
			comp2 = comp2Entry.get()
			comp2 = errorCheck(comp2)
			comp3 = comp3Entry.get()
			comp3 = errorCheck(comp3)
			if isinstance(mag1, float) and isinstance(mag2,float) and isinstance(mag3, float) and isinstance(mag4, float) and isinstance(dir1,float) and isinstance(dir2, float) and isinstance(dir3, float) and isinstance(dir4, float) and comp1 == '+' or comp1 == '-' and comp2 == '+' or comp2 == '+' and comp3 == '+' or comp3 == '-':
				componentsList = []
				operationList = []
				xComponent1 = mag1
				yComponent1 = dir1
				xComponent2 = mag2
				yComponent2 = dir2
				xComponent3 = mag3
				yComponent3 = dir3
				xComponent4 = mag4
				yComponent4 = dir4
				componentsList.append(xComponent1)
				componentsList.append(yComponent1)
				componentsList.append(xComponent2)
				componentsList.append(yComponent2)
				componentsList.append(xComponent3)
				componentsList.append(yComponent3)
				componentsList.append(xComponent4)
				componentsList.append(yComponent4)
				operationList.append(comp1)
				operationList.append(comp2)
				operationList.append(comp3)
				numVec = 4
				vectorCalc()
			else: 
				error_label = tk.Label(master = vectorMenu3, height = 2, width = 30, foreground = 'red', background = 'black', text = 'ERROR: One or more values are incorrect')
				error_label.place(x=135, y=400)
		start1 = tk.Button(master = vectorMenu3, command = checker4, height = 2, width = 10, text = 'START')
		start1.place(x=200,y=450)
	two_button = tk.Button(master = vectorMenu2, command = two_vectors, height = 2, width = 10, text = '2')
	two_button.place(x=60, y=150)
	three_button = tk.Button(master = vectorMenu2, command = three_vectors, height = 2, width = 10, text = '3')
	three_button.place(x=210, y=150)
	four_button = tk.Button(master = vectorMenu2, command = four_vectors, height = 2, width = 10, text = '4')
	four_button.place(x=350, y=150)

def vectorMenu():
	vectorMenu1 = tk.Tk()
	vectorMenu1.geometry('500x500')
	vectorLabel = tk.Label(master = vectorMenu1, text = 'How you would like to input your vectors?', font=('bold'),width = 50, height = 5, fg = 'black')
	vectorLabel.pack()
	mag_button = tk.Button(master = vectorMenu1, command = magVectors, height = 2, width = 10, text = 'Magnitude')
	mag_button.place(x=100,y=150)
	comp_button = tk.Button(master = vectorMenu1, command = compVectors, height = 2, width = 10, text = 'Components')
	comp_button.place(x=300,y=150)

window = tk.Tk()
window.geometry('800x750')
window.resizable(False,False)
title = tk.Label(text= 'Vectors, Velocites, Visualizations', font =("Unispace", 24,),foreground = 'black',  width = 25, height = 7)
title.pack(fill=tk.X)
plot_button = tk.Button(master = window, command = openVar, font=('bold'),height = 2, width = 25, text = "Projectile Motion Visualizer")
plot_button.place(x=260, y=375)
instructions_button = tk.Button(master = window, command = instructions, font=('bold'),height = 2, width = 10, text = "Instructions")
instructions_button.place(x=320, y=600)
balls_button = tk.Button(master = window, command = fourBallsMenu, font=('bold'),height = 2, width = 20, text = "Parameters Comparison")
balls_button.place(x=500, y=500)
solver_button = tk.Button(master = window, command = vectorMenu, font=('bold'),height = 2, width = 15, text = 'Vector Visualizer')
solver_button.place(x=100, y=500)
window.mainloop()