##  Bare Metal AutoScaling Based On OpenStack Ironic


### setup tacker-ironic devstack

ref: <https://docs.openstack.org/developer/ironic/mitaka/drivers/vbox.html>

NOTICE: 
+ Install `pyremotevbox` before run stack.sh, or will ends failure !
+ After configure baremetal network, restart all neutron service, other than only q-agt, or will can't create net.


### windows virtualbox webSrv

ip: 10.0.2.2 port: 18083


### ironic usage

`ironic node-create -d pxe_vbox -i virtualbox_host='10.0.2.2' -i virtualbox_vmname='baremetal'`

`ironic port-create -n $NODE_UUID -a $MAC_ADDRESS`

`ironic node-update $NODE_UUID add driver_info/deploy_kernel=$DEPLOY_VMLINUZ_UUID driver_info/deploy_ramdisk=$DEPLOY_INITRD_UUID`

(exec `glance image-list` to get DEPLOY_VMLNUZ_UUID)

`ironic node-validate $NODE_UUID`

`nova boot --config-drive true --flavor baremetal --image cirros-0.3.4-x86_64-uec bm`

