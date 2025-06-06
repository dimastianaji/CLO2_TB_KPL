from transitions import Machine

states = ['Created', 'Completed', 'Expired']

def buat_fsm(task):
    fsm = Machine(model=task, states=states, initial='Created')
    fsm.add_transition('complete', 'Created', 'Completed', after=lambda: setattr(task, 'status', 'Completed'))
    fsm.add_transition('expire', 'Created', 'Expired', after=lambda: setattr(task, 'status', 'Expired'))
    return fsm
