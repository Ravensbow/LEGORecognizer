funciton onParadeStart()

    sf=ldc.subfile()

    pieceCounter = 1
    cameraLoopCounter = 1
    frameCounter = 1

    myFPS = 8
    cameraAngleIncrement = 360/myFPS

    unviewPosition = ldc.vector()
    unviewPosition:set(10000,10000,10000)
    viewPosition = ldc.vector()
    viewPosition:set(25,25,25)


    cam=ldc.view():getCamera()
    camPos=ldc.vector()
    camPos:set(50,-50,50)
    camDist = 1350
    cam:setThirdPerson(camPos, camDist, 0, 0, 0)
    cam:apply(0)

    refCnt=sf:getRefCount()
    for i=0,refCnt do
        sf:getRef(i):setPos(unviewPosition)
    end

    sf:getRef(1):setPos(viewPosition)
end