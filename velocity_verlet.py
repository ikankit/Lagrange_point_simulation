from acceleration import body_acc
def velocity_verlet( bodies, dt):
    
    #old values
    for body in bodies:
        body.acc_old= body_acc(body, bodies)
    
    for body in bodies:
        body.position=(body.position+body.velocity*dt+ 0.5*body.acc_old*dt**2)
    
    for body in bodies:
        body.acc_new= body_acc(body, bodies)
        
    for body in bodies:
        body.velocity= (body.velocity+0.5*(body.acc_old+body.acc_new)*dt)
    
    return bodies