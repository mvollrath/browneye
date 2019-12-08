Name:       libnl
Version:    3.4.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/genl-ctrl-list
/usr/bin/idiag-socket-details
/usr/bin/nf-ct-add
/usr/bin/nf-ct-list
/usr/bin/nf-exp-add
/usr/bin/nf-exp-delete
/usr/bin/nf-exp-list
/usr/bin/nf-log
/usr/bin/nf-monitor
/usr/bin/nf-queue
/usr/bin/nl-addr-add
/usr/bin/nl-addr-delete
/usr/bin/nl-addr-list
/usr/bin/nl-class-add
/usr/bin/nl-class-delete
/usr/bin/nl-class-list
/usr/bin/nl-classid-lookup
/usr/bin/nl-cls-add
/usr/bin/nl-cls-delete
/usr/bin/nl-cls-list
/usr/bin/nl-fib-lookup
/usr/bin/nl-link-enslave
/usr/bin/nl-link-ifindex2name
/usr/bin/nl-link-list
/usr/bin/nl-link-name2ifindex
/usr/bin/nl-link-release
/usr/bin/nl-link-set
/usr/bin/nl-link-stats
/usr/bin/nl-list-caches
/usr/bin/nl-list-sockets
/usr/bin/nl-monitor
/usr/bin/nl-neigh-add
/usr/bin/nl-neigh-delete
/usr/bin/nl-neigh-list
/usr/bin/nl-neightbl-list
/usr/bin/nl-pktloc-lookup
/usr/bin/nl-qdisc-add
/usr/bin/nl-qdisc-delete
/usr/bin/nl-qdisc-list
/usr/bin/nl-route-add
/usr/bin/nl-route-delete
/usr/bin/nl-route-get
/usr/bin/nl-route-list
/usr/bin/nl-rule-list
/usr/bin/nl-tctree-list
/usr/bin/nl-util-addr
/usr/etc/libnl/classid
/usr/etc/libnl/pktloc
/usr/include/libnl3/netlink/addr.h
/usr/include/libnl3/netlink/attr.h
/usr/include/libnl3/netlink/cache-api.h
/usr/include/libnl3/netlink/cache.h
/usr/include/libnl3/netlink/cli/addr.h
/usr/include/libnl3/netlink/cli/class.h
/usr/include/libnl3/netlink/cli/cls.h
/usr/include/libnl3/netlink/cli/ct.h
/usr/include/libnl3/netlink/cli/exp.h
/usr/include/libnl3/netlink/cli/link.h
/usr/include/libnl3/netlink/cli/neigh.h
/usr/include/libnl3/netlink/cli/qdisc.h
/usr/include/libnl3/netlink/cli/route.h
/usr/include/libnl3/netlink/cli/rule.h
/usr/include/libnl3/netlink/cli/tc.h
/usr/include/libnl3/netlink/cli/utils.h
/usr/include/libnl3/netlink/data.h
/usr/include/libnl3/netlink/errno.h
/usr/include/libnl3/netlink/fib_lookup/lookup.h
/usr/include/libnl3/netlink/fib_lookup/request.h
/usr/include/libnl3/netlink/genl/ctrl.h
/usr/include/libnl3/netlink/genl/family.h
/usr/include/libnl3/netlink/genl/genl.h
/usr/include/libnl3/netlink/genl/mngt.h
/usr/include/libnl3/netlink/handlers.h
/usr/include/libnl3/netlink/hash.h
/usr/include/libnl3/netlink/hashtable.h
/usr/include/libnl3/netlink/idiag/idiagnl.h
/usr/include/libnl3/netlink/idiag/meminfo.h
/usr/include/libnl3/netlink/idiag/msg.h
/usr/include/libnl3/netlink/idiag/req.h
/usr/include/libnl3/netlink/idiag/vegasinfo.h
/usr/include/libnl3/netlink/list.h
/usr/include/libnl3/netlink/msg.h
/usr/include/libnl3/netlink/netfilter/ct.h
/usr/include/libnl3/netlink/netfilter/exp.h
/usr/include/libnl3/netlink/netfilter/log.h
/usr/include/libnl3/netlink/netfilter/log_msg.h
/usr/include/libnl3/netlink/netfilter/netfilter.h
/usr/include/libnl3/netlink/netfilter/nfnl.h
/usr/include/libnl3/netlink/netfilter/queue.h
/usr/include/libnl3/netlink/netfilter/queue_msg.h
/usr/include/libnl3/netlink/netlink-compat.h
/usr/include/libnl3/netlink/netlink-kernel.h
/usr/include/libnl3/netlink/netlink.h
/usr/include/libnl3/netlink/object-api.h
/usr/include/libnl3/netlink/object.h
/usr/include/libnl3/netlink/route/act/gact.h
/usr/include/libnl3/netlink/route/act/mirred.h
/usr/include/libnl3/netlink/route/act/skbedit.h
/usr/include/libnl3/netlink/route/action.h
/usr/include/libnl3/netlink/route/addr.h
/usr/include/libnl3/netlink/route/class.h
/usr/include/libnl3/netlink/route/classifier.h
/usr/include/libnl3/netlink/route/cls/basic.h
/usr/include/libnl3/netlink/route/cls/cgroup.h
/usr/include/libnl3/netlink/route/cls/ematch.h
/usr/include/libnl3/netlink/route/cls/ematch/cmp.h
/usr/include/libnl3/netlink/route/cls/ematch/meta.h
/usr/include/libnl3/netlink/route/cls/ematch/nbyte.h
/usr/include/libnl3/netlink/route/cls/ematch/text.h
/usr/include/libnl3/netlink/route/cls/fw.h
/usr/include/libnl3/netlink/route/cls/police.h
/usr/include/libnl3/netlink/route/cls/u32.h
/usr/include/libnl3/netlink/route/link.h
/usr/include/libnl3/netlink/route/link/api.h
/usr/include/libnl3/netlink/route/link/bonding.h
/usr/include/libnl3/netlink/route/link/bridge.h
/usr/include/libnl3/netlink/route/link/can.h
/usr/include/libnl3/netlink/route/link/inet.h
/usr/include/libnl3/netlink/route/link/inet6.h
/usr/include/libnl3/netlink/route/link/info-api.h
/usr/include/libnl3/netlink/route/link/ip6tnl.h
/usr/include/libnl3/netlink/route/link/ipgre.h
/usr/include/libnl3/netlink/route/link/ipip.h
/usr/include/libnl3/netlink/route/link/ipvlan.h
/usr/include/libnl3/netlink/route/link/ipvti.h
/usr/include/libnl3/netlink/route/link/macsec.h
/usr/include/libnl3/netlink/route/link/macvlan.h
/usr/include/libnl3/netlink/route/link/macvtap.h
/usr/include/libnl3/netlink/route/link/ppp.h
/usr/include/libnl3/netlink/route/link/sit.h
/usr/include/libnl3/netlink/route/link/sriov.h
/usr/include/libnl3/netlink/route/link/veth.h
/usr/include/libnl3/netlink/route/link/vlan.h
/usr/include/libnl3/netlink/route/link/vrf.h
/usr/include/libnl3/netlink/route/link/vxlan.h
/usr/include/libnl3/netlink/route/neighbour.h
/usr/include/libnl3/netlink/route/neightbl.h
/usr/include/libnl3/netlink/route/netconf.h
/usr/include/libnl3/netlink/route/nexthop.h
/usr/include/libnl3/netlink/route/pktloc.h
/usr/include/libnl3/netlink/route/qdisc.h
/usr/include/libnl3/netlink/route/qdisc/cbq.h
/usr/include/libnl3/netlink/route/qdisc/dsmark.h
/usr/include/libnl3/netlink/route/qdisc/fifo.h
/usr/include/libnl3/netlink/route/qdisc/fq_codel.h
/usr/include/libnl3/netlink/route/qdisc/hfsc.h
/usr/include/libnl3/netlink/route/qdisc/htb.h
/usr/include/libnl3/netlink/route/qdisc/netem.h
/usr/include/libnl3/netlink/route/qdisc/plug.h
/usr/include/libnl3/netlink/route/qdisc/prio.h
/usr/include/libnl3/netlink/route/qdisc/red.h
/usr/include/libnl3/netlink/route/qdisc/sfq.h
/usr/include/libnl3/netlink/route/qdisc/tbf.h
/usr/include/libnl3/netlink/route/route.h
/usr/include/libnl3/netlink/route/rtnl.h
/usr/include/libnl3/netlink/route/rule.h
/usr/include/libnl3/netlink/route/tc-api.h
/usr/include/libnl3/netlink/route/tc.h
/usr/include/libnl3/netlink/socket.h
/usr/include/libnl3/netlink/types.h
/usr/include/libnl3/netlink/utils.h
/usr/include/libnl3/netlink/version.h
/usr/include/libnl3/netlink/xfrm/ae.h
/usr/include/libnl3/netlink/xfrm/lifetime.h
/usr/include/libnl3/netlink/xfrm/sa.h
/usr/include/libnl3/netlink/xfrm/selector.h
/usr/include/libnl3/netlink/xfrm/sp.h
/usr/include/libnl3/netlink/xfrm/template.h
/usr/lib64/libnl-3.la
/usr/lib64/libnl-3.so
/usr/lib64/libnl-3.so.200
/usr/lib64/libnl-3.so.200.26.0
/usr/lib64/libnl-cli-3.la
/usr/lib64/libnl-cli-3.so
/usr/lib64/libnl-cli-3.so.200
/usr/lib64/libnl-cli-3.so.200.26.0
/usr/lib64/libnl-genl-3.la
/usr/lib64/libnl-genl-3.so
/usr/lib64/libnl-genl-3.so.200
/usr/lib64/libnl-genl-3.so.200.26.0
/usr/lib64/libnl-idiag-3.la
/usr/lib64/libnl-idiag-3.so
/usr/lib64/libnl-idiag-3.so.200
/usr/lib64/libnl-idiag-3.so.200.26.0
/usr/lib64/libnl-nf-3.la
/usr/lib64/libnl-nf-3.so
/usr/lib64/libnl-nf-3.so.200
/usr/lib64/libnl-nf-3.so.200.26.0
/usr/lib64/libnl-route-3.la
/usr/lib64/libnl-route-3.so
/usr/lib64/libnl-route-3.so.200
/usr/lib64/libnl-route-3.so.200.26.0
/usr/lib64/libnl-xfrm-3.la
/usr/lib64/libnl-xfrm-3.so
/usr/lib64/libnl-xfrm-3.so.200
/usr/lib64/libnl-xfrm-3.so.200.26.0
/usr/lib64/libnl/cli/cls/basic.la
/usr/lib64/libnl/cli/cls/basic.so
/usr/lib64/libnl/cli/cls/cgroup.la
/usr/lib64/libnl/cli/cls/cgroup.so
/usr/lib64/libnl/cli/qdisc/bfifo.la
/usr/lib64/libnl/cli/qdisc/bfifo.so
/usr/lib64/libnl/cli/qdisc/blackhole.la
/usr/lib64/libnl/cli/qdisc/blackhole.so
/usr/lib64/libnl/cli/qdisc/fq_codel.la
/usr/lib64/libnl/cli/qdisc/fq_codel.so
/usr/lib64/libnl/cli/qdisc/hfsc.la
/usr/lib64/libnl/cli/qdisc/hfsc.so
/usr/lib64/libnl/cli/qdisc/htb.la
/usr/lib64/libnl/cli/qdisc/htb.so
/usr/lib64/libnl/cli/qdisc/ingress.la
/usr/lib64/libnl/cli/qdisc/ingress.so
/usr/lib64/libnl/cli/qdisc/pfifo.la
/usr/lib64/libnl/cli/qdisc/pfifo.so
/usr/lib64/libnl/cli/qdisc/plug.la
/usr/lib64/libnl/cli/qdisc/plug.so
/usr/lib64/pkgconfig/libnl-3.0.pc
/usr/lib64/pkgconfig/libnl-cli-3.0.pc
/usr/lib64/pkgconfig/libnl-genl-3.0.pc
/usr/lib64/pkgconfig/libnl-idiag-3.0.pc
/usr/lib64/pkgconfig/libnl-nf-3.0.pc
/usr/lib64/pkgconfig/libnl-route-3.0.pc
/usr/lib64/pkgconfig/libnl-xfrm-3.0.pc
/usr/share/man/man8/genl-ctrl-list.8.gz
/usr/share/man/man8/nl-classid-lookup.8.gz
/usr/share/man/man8/nl-pktloc-lookup.8.gz
/usr/share/man/man8/nl-qdisc-add.8.gz
/usr/share/man/man8/nl-qdisc-delete.8.gz
/usr/share/man/man8/nl-qdisc-list.8.gz

%changelog
# let's skip this for now
