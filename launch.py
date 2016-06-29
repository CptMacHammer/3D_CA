import planeGenerator
import movementSimulator
from threading import Thread
import centralizedComm
import decentralizedComm
import defaultValues
import logging
import standardFuncs


#
def main():
    standardFuncs.logger()

    logging.info('Started')

    # Check to see if the simulation is ran in a centralized or decentralized manner.
    if not defaultValues.CENTRALIZED:
        communicator = decentralizedComm.synchronizer()
    else:
        communicator = centralizedComm.uavComm()

    communicator.start()

    # Generate a number of plane threads with n waypoints in a specified grid size.
    plane = planeGenerator.generate_planes(
        defaultValues.NUM_PLANES,
        defaultValues.NUM_WAY_POINTS,
        defaultValues.GRID_SIZE,
        communicator
    )
    logging.info('Finished')


if __name__ == '__main__':
    main()
