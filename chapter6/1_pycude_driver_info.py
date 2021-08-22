import pycuda.driver as drv
drv.init()

print("%d device(s) found" % drv.Device.count())
for oridinal in range(drv.Device.count()):
    dev = drv.Device(oridinal)
    print("Device # %d: %s" %(oridinal, dev.name()))
    print("Compute Capablility: %d.%d" % dev.compute_capability())
    print("Total Memory: %d KB" % (dev.total_memory()//1024))