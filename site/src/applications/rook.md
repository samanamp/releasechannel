# Rook

<div>
<demo-component app-code="rook"/>
</div>


## v1.6.3
<p style="font-size:12px;"> 21, May 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.6.3" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>Improvements</h1>
<p>Rook v1.6.3 is a patch release limited in scope and focusing on small feature additions and bug fixes.</p>
<h2>Ceph</h2>
<ul>
<li>Ensure correct devices are started for OSDs after node restart (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7951">#7951</a>, <a class="user-mention" href="https://github.com/BlaineEXE">@BlaineEXE</a>)</li>
<li>Write reconcile results to events on the CephCluster CR (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7222">#7222</a>, <a class="user-mention" href="https://github.com/iamniting">@iamniting</a>)</li>
<li>Updated dashboard ingress example for networking v1 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7933">#7933</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Remove obsolete gateway type setting in object store CRD (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7919">#7919</a>, <a class="user-mention" href="https://github.com/satoru-takeuchi">@satoru-takeuchi</a>)</li>
<li>Support specifying only public network or only cluster network or both (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7546">#7546</a>, <a class="user-mention" href="https://github.com/rohan47">@rohan47</a>)</li>
<li>Generate same operator deployment for OKD as OCP (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7898">#7898</a>, <a class="user-mention" href="https://github.com/RyuunoAelia">@RyuunoAelia</a>)</li>
<li>Ensure correct hostpath lock for OSD integrity (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7886">#7886</a>, <a class="user-mention" href="https://github.com/satoru-takeuchi">@satoru-takeuchi</a>)</li>
<li>Improve resilience of mon failover if operator is restarted during failover (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7884">#7884</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Disallow overriding the liveness probe handler function (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7889">#7889</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Actively update the service endpoint for external mgr (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7875">#7875</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Remove obsolete CSI statefulset template path vars from K8s 1.13 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7877">#7877</a>, <a class="user-mention" href="https://github.com/Rakshith-R">@Rakshith-R</a>)</li>
<li>Create crash collector pods after mon secret created (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7867">#7867</a>, <a class="user-mention" href="https://github.com/subhamkrai">@subhamkrai</a>)</li>
<li>OSD controller only updates PDBs during node drains instead of any OSD down event (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7726">#7726</a>, <a class="user-mention" href="https://github.com/sp98">@sp98</a>)</li>
<li>Allow heap dump generation when logCollector sidecar is not running (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7847">#7847</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Add nullable to object gateway settings (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7857">#7857</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
</ul>

## v1.6.2
<p style="font-size:12px;"> 07, May 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.6.2" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>Improvements</h1>
<p>Rook v1.6.2 is a patch release limited in scope and focusing on small feature additions and bug fixes.</p>
<h2>Ceph</h2>
<ul>
<li>Set base Ceph operator image and example deployments to v16.2.2 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7829">#7829</a>, <a class="user-mention" href="https://github.com/BlaineEXE">@BlaineEXE</a>)</li>
<li>Update snapshot APIs from v1beta1 to v1 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7711">#7711</a>, <a class="user-mention" href="https://github.com/Rakshith-R">@Rakshith-R</a>)</li>
<li>Documentation for creating static PVs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7782">#7782</a>, <a class="user-mention" href="https://github.com/Rakshith-R">@Rakshith-R</a>)</li>
<li>Allow setting primary-affinity for the OSD (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7807">#7807</a>, <a class="user-mention" href="https://github.com/synarete">@synarete</a>)</li>
<li>Remove unneeded debug log statements (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7526">#7526</a>, <a class="user-mention" href="https://github.com/parth-gr">@parth-gr</a>)</li>
<li>Preserve volume claim template annotations during upgrade (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7835">#7835</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Allow re-creating erasure coded pool with different settings (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7820">#7820</a>, <a class="user-mention" href="https://github.com/subhamkrai">@subhamkrai</a>)</li>
<li>Double mon failover timeout during a node drain (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7801">#7801</a>, <a class="user-mention" href="https://github.com/sp98">@sp98</a>)</li>
<li>Remove unused volumesource schema from CephCluster CRD (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7813">#7813</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Set the device class on raw mode osds (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7815">#7815</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>External cluster schema fix to allow not setting mons (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7789">#7789</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Add phase to the CephFilesystem CRD (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7752">#7752</a>, <a class="user-mention" href="https://github.com/jshen28">@jshen28</a>)</li>
<li>Generate full schema for volumeClaimTemplates in the CephCluster CRD (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7631">#7631</a>, <a class="user-mention" href="https://github.com/BlaineEXE">@BlaineEXE</a>)</li>
<li>Automate upgrades for the MDS daemon to properly scale down and scale up (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7445">#7445</a>, <a class="user-mention" href="https://github.com/jshen28">@jshen28</a>)</li>
<li>Add Vault KMS support for object stores (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7385">#7385</a>, <a class="user-mention" href="https://github.com/thotz">@thotz</a>)</li>
<li>Ensure object store endpoint is initialized when creating an object user (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7633">#7633</a>, <a class="user-mention" href="https://github.com/alimaredia">@alimaredia</a>)</li>
<li>Support for OBC operations when RGW is configured with TLS (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7764">#7764</a>, <a class="user-mention" href="https://github.com/thotz">@thotz</a>)</li>
<li>Preserve the OSD topology affinity during upgrade for clusters on PVCs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7759">#7759</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Unify timeouts for various Ceph commands (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7719">#7719</a>, <a class="user-mention" href="https://github.com/satoru-takeuchi">@satoru-takeuchi</a>)</li>
<li>Allow setting annotations on RGW service (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7598">#7598</a>, <a class="user-mention" href="https://github.com/thotz">@thotz</a>)</li>
<li>Expand PVC size of mon daemons if requested (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7715">#7715</a>, <a class="user-mention" href="https://github.com/iamniting">@iamniting</a>)</li>
</ul>

## v1.5.11
<p style="font-size:12px;"> 04, May 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.5.11" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>Improvements</h1>
<p>Rook v1.5.11 is a patch release limited in scope and focusing on small feature additions and bug fixes.</p>
<h2>Ceph</h2>
<ul>
<li>Set operator base image and default Ceph version to v15.2.11 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7733">#7733</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Deploy Ceph-CSI v3.2.2 with latest base image including CVE fixes (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7810">#7810</a>, <a class="user-mention" href="https://github.com/Madhu-1">@Madhu-1</a>)</li>
<li>Improve node watcher for deploying new OSDs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/issues/7462">#7462</a>, <a class="user-mention" href="https://github.com/parth-gr">@parth-gr</a>)</li>
<li>Fix bucket health check where SSL is enabled for RGW (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7331">#7331</a>, <a class="user-mention" href="https://github.com/thotz">@thotz</a>)</li>
<li>Detect the topology affinity for portable OSDs during upgrade (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7759">#7759</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Ensure object store endpoint is initialized for user (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7633">#7633</a>, <a class="user-mention" href="https://github.com/alimaredia">@alimaredia</a>)</li>
</ul>

## v1.6.1
<p style="font-size:12px;"> 22, Apr 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.6.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>Improvements</h1>
<p>Rook v1.6.1 is a patch release limited in scope and focusing on small feature additions and bug fixes.</p>
<h2>Ceph</h2>
<ul>
<li>Disable host networking by default in the CSI plugin with option to enable (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7356">#7356</a>, <a class="user-mention" href="https://github.com/Rakshith-R">@Rakshith-R</a>)</li>
<li>Fix the schema for erasure-coded pools so replication size is not required (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7662">#7662</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Improve node watcher for adding new OSDs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7568">#7568</a>, <a class="user-mention" href="https://github.com/parth-gr">@parth-gr</a>)</li>
<li>Operator base image updated to v16.2.1 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7713">#7713</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Deployment examples updated to Ceph v15.2.11 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7733">#7733</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Update Ceph-CSI to v3.3.1 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7724">#7724</a>, <a class="user-mention" href="https://github.com/Madhu-1">@Madhu-1</a>)</li>
<li>Allow any device class for the OSDs in a pool instead of restricting the schema (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7718">#7718</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Fix metadata OSDs for Ceph Pacific (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7703">#7703</a>, <a class="user-mention" href="https://github.com/BlaineEXE">@BlaineEXE</a>)</li>
<li>Allow setting the initial CRUSH weight for an OSD (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7472">#7472</a>, <a class="user-mention" href="https://github.com/synarete">@synarete</a>)</li>
<li>Fix object store health check in case SSL is enabled (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7331">#7331</a>, <a class="user-mention" href="https://github.com/thotz">@thotz</a>)</li>
<li>Upgrades now ensure latest config flags are set for MDS and RGW (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7681">#7681</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Suppress noisy RGW log entry for radosgw-admin commands (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7663">#7663</a>, <a class="user-mention" href="https://github.com/BlaineEXE">@BlaineEXE</a>)</li>
</ul>

## v1.5.10
<p style="font-size:12px;"> 16, Apr 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.5.10" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>Improvements</h1>
<p>Rook v1.5.10 is a patch release limited in scope and focusing on small feature additions and bug fixes.</p>
<h2>Ceph</h2>
<ul>
<li>Update Ceph-CSI to v3.2.1 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7506">#7506</a>, <a class="user-mention" href="https://github.com/shaas">@shaas</a>)</li>
<li>Use latest Ceph API for setting dashboard and rgw credentials (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7641">#7641</a>, <a class="user-mention" href="https://github.com/subhamkrai">@subhamkrai</a>)</li>
<li>Redact secret info from reconcile diffs in debug logs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7630">#7630</a>, <a class="user-mention" href="https://github.com/BlaineEXE">@BlaineEXE</a>)</li>
<li>Continue to get available devices if failed to get a device info (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7608">#7608</a>, <a class="user-mention" href="https://github.com/satoru-takeuchi">@satoru-takeuchi</a>)</li>
<li>Include RGW pods in list for rescheduling from failed node (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7537">#7537</a>, <a class="user-mention" href="https://github.com/rohan47">@rohan47</a>)</li>
<li>Enforce pg_auto_scaler on rgw pools (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7513">#7513</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Prevent voluntary mon drain while another mon is failing over (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7442">#7442</a>, <a class="user-mention" href="https://github.com/sp98">@sp98</a>)</li>
<li>Avoid restarting all encrypted OSDs on cluster growth (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7489">#7489</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Set secret type on external cluster script (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7473">#7473</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Fix init container "expand-encrypted-bluefs" for encrypted OSDs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7466">#7466</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Fail pool creation if the sub failure domain is the same as the failure domain (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7284">#7284</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Set default backend for vault and remove temp key for encrypted OSDs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7454">#7454</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
</ul>

## v1.6.0
<p style="font-size:12px;"> 16, Apr 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.6.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>Major Themes</h1>
<p>v1.6.0 is a minor release with features primarily for the Ceph operator.</p>
<h2>K8s Version Support</h2>
<p>Kubernetes supported versions: 1.11 and newer</p>
<h2>Upgrade Guides</h2>
<p>If you are running a previous Rook version, please see the corresponding storage provider upgrade guide:</p>
<ul>
<li><a href="https://rook.github.io/docs/rook/v1.6/ceph-upgrade.html" rel="nofollow">Ceph</a></li>
</ul>
<h2>Breaking Changes</h2>
<h3>Removed Storage Providers</h3>
<p>Each storage provider is unique and requires time and attention to properly develop and support. After much discussion with the community, we have decided to remove three storage providers from Rook in order to focus our efforts on storage providers that have active community support. See the <a href="https://github.com/rook/rook#project-status">project status</a> for more information. These storage providers have been removed:</p>
<ul>
<li>CockroachDB</li>
<li>EdgeFS</li>
<li>YugabyteDB</li>
</ul>
<h3>Ceph</h3>
<ul>
<li>Support for creating OSDs via Drive Groups was removed. Please refer to the <a href="https://rook.github.io/docs/rook/v1.6/ceph-upgrade.html#migrate-the-drive-group-spec" rel="nofollow">Ceph upgrade guide</a> for migration instructions.</li>
</ul>
<h2>Features</h2>
<h3>Ceph</h3>
<ul>
<li>Ceph Pacific (v16) support, including features such as:
<ul>
<li>Multiple Ceph Filesystems</li>
<li>Networking dual stack</li>
</ul>
</li>
<li><a href="https://rook.github.io/docs/rook/v1.6/ceph-fs-mirror-crd.html" rel="nofollow">CephFilesystemMirror CRD</a> to support mirroring of CephFS volumes with Pacific</li>
<li>Ceph CSI Driver
<ul>
<li>CSI v3.3.0 driver enabled by default</li>
<li><a href="https://rook.github.io/docs/rook/v1.6/ceph-csi-drivers.html#rbd-mirroring" rel="nofollow">Volume Replication Controller</a> for improved RBD replication support</li>
<li>Multus support</li>
<li>GRPC metrics disabled by default</li>
</ul>
</li>
<li>Ceph RGW
<ul>
<li>Extended the support of vault KMS configuration</li>
<li>Scale with multiple daemons with a single deployment instead of a separate deployment for each rgw daemon</li>
</ul>
</li>
<li>OSDs:
<ul>
<li>LVM is no longer used to provision OSDs as of Nautilus 14.2.14 Octopus 15.2.9, and Pacific 16.2.0, simplifying the OSDs on raw devices, except for encrypted OSDs and multiple OSDs per device.</li>
<li>More efficient updates for multiple OSDs at the same time (in the same failure domain) to speed up upgrades for larger Ceph clusters</li>
</ul>
</li>
<li>Multiple Ceph mgr daemons are supported for stretch clusters and other clusters where HA of the mgr is critical (set <code>count: 2</code> under <code>mgr</code> in the CephCluster CR)</li>
<li>Pod Disruption Budgets (PDBs) are enabled by default for Mon, RGW, MDS, and OSD daemons. See the <a href="https://rook.github.io/docs/rook/v1.6/ceph-cluster-crd.html#cluster-settings" rel="nofollow">disruption management</a> settings.</li>
<li>Monitor failover can be <a href="https://rook.github.io/docs/rook/v1.6/ceph-mon-health.html#failing-over-a-monitor" rel="nofollow">disabled</a>, for scenarios where maintenance is planned and automatic mon failover is not desired</li>
<li>CephClient CRD has been converted to use the controller-runtime library</li>
</ul>

## v1.6.0-beta.0
<p style="font-size:12px;"> 07, Apr 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.6.0-beta.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>release v1.6.0-beta.0</p>

## v1.6.0-alpha.0
<p style="font-size:12px;"> 07, Apr 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.6.0-alpha.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>release v1.6.0-alpha.0</p>

## v1.5.9
<p style="font-size:12px;"> 18, Mar 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.5.9" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>Improvements</h1>
<p>Rook v1.5.9 is a patch release limited in scope and focusing on small feature additions and bug fixes.</p>
<h2>Ceph</h2>
<ul>
<li>Properly add CephCluster schema to support bucket health checks (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7330">#7330</a>, <a class="user-mention" href="https://github.com/thotz">@thotz</a>)</li>
<li>Avoid overlapping OSD placement for PVC and non-PVCs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7415">#7415</a>, <a class="user-mention" href="https://github.com/subhamkrai">@subhamkrai</a>)</li>
<li>Correct RBAC for multus in the helm chart (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7340">#7340</a>, <a class="user-mention" href="https://github.com/rohan47">@rohan47</a>)</li>
<li>During uninstall skip cleanup if cluster is not configured correctly (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7414">#7414</a>, <a class="user-mention" href="https://github.com/sp98">@sp98</a>)</li>
<li>Enable the PG auto repair module (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7391">#7391</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Set pool quota with K8s quantity format (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7397">#7397</a>, <a class="user-mention" href="https://github.com/fritchie">@fritchie</a>)</li>
<li>Proper JSON parsing for object store configuration (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7354">#7354</a>, <a class="user-mention" href="https://github.com/satoru-takeuchi">@satoru-takeuchi</a>)</li>
<li>Disable CSI GRPC metrics by default (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7379">#7379</a>, <a class="user-mention" href="https://github.com/Madhu-1">@Madhu-1</a>)</li>
<li>Add OSD flapping alert (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7358">#7358</a>, <a class="user-mention" href="https://github.com/anmolsachan">@anmolsachan</a>)</li>
<li>Add OSD slow ops alert (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7417">#7417</a>, <a class="user-mention" href="https://github.com/anmolsachan">@anmolsachan</a>)</li>
<li>Prometheus query to avoid many-to-many match error (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7273">#7273</a>, <a class="user-mention" href="https://github.com/anmolsachan">@anmolsachan</a>)</li>
<li>Only raise CephCluster conditions that represent current state (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7315">#7315</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Handle SSL cases for RGW's liveness probe (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7334">#7334</a>, <a class="user-mention" href="https://github.com/thotz">@thotz</a>)</li>
<li>Improved vault warnings for encrypted OSDs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7337">#7337</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Stop managing labels of monitoring resources (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7323">#7323</a>, <a class="user-mention" href="https://github.com/umangachapagain">@umangachapagain</a>)</li>
<li>Detect standby mgr for external clusters (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7217">#7217</a>, <a class="user-mention" href="https://github.com/aruniiird">@aruniiird</a>)</li>
</ul>

## v1.5.8
<p style="font-size:12px;"> 26, Feb 2021 
<a href="https://github.com/rook/rook/releases/tag/v1.5.8" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>Improvements</h1>
<p>Rook v1.5.8 is a patch release limited in scope and focusing on small feature additions and bug fixes.</p>
<h2>Ceph</h2>
<ul>
<li>Update operator and example manifests to use ceph/ceph:v15.2.9 (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7302">#7302</a>, <a class="user-mention" href="https://github.com/BlaineEXE">@BlaineEXE</a>)</li>
<li>Consistently force delete Rook pods on unresponsive nodes (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7266">#7266</a>, <a class="user-mention" href="https://github.com/rohan47">@rohan47</a>)</li>
<li>OSD encryption improvements with Vault (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7292">#7292</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Ability to set pool quotas in bytes or objects (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7264">#7264</a>, <a class="user-mention" href="https://github.com/fritchie">@fritchie</a>)</li>
<li>Fix SIGSEGV when failing to get object store user (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7280">#7280</a>, <a class="user-mention" href="https://github.com/satoru-takeuchi">@satoru-takeuchi</a>)</li>
<li>Enforce portable OSDs in same topology as osd prepare job (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7256">#7256</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Do not merge nodeAffinity for OSDs between device sets and non-device sets (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7192">#7192</a>, <a class="user-mention" href="https://github.com/subhamkrai">@subhamkrai</a>)</li>
<li>During OSD removal archive crash dumps (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7001">#7001</a>, <a class="user-mention" href="https://github.com/crombus">@crombus</a>)</li>
<li>Add tolerations for all daemons to the cleanup job (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7234">#7234</a>, <a class="user-mention" href="https://github.com/travisn">@travisn</a>)</li>
<li>Helm fix for casing on enableCephFSSnapshotter (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7249">#7249</a>, <a class="user-mention" href="https://github.com/subhamkrai">@subhamkrai</a>)</li>
<li>Do not override existing Vault keys for encrypted OSDs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7245">#7245</a>, <a class="user-mention" href="https://github.com/leseb">@leseb</a>)</li>
<li>Create new OSDs before updating existing OSDs (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/6926">#6926</a>, <a class="user-mention" href="https://github.com/BlaineEXE">@BlaineEXE</a>)</li>
<li>Helm fix to allow multiple filesystems (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7224">#7224</a>, <a class="user-mention" href="https://github.com/TomHellier">@TomHellier</a>)</li>
<li>Add the secure endpoint to the object store user CR status (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7191">#7191</a>, <a class="user-mention" href="https://github.com/thotz">@thotz</a>)</li>
<li>Set default values to allow partial override of liveness probes (<a class="issue-link js-issue-link" href="https://github.com/rook/rook/pull/7215">#7215</a>, <a class="user-mention" href="https://github.com/subhamkrai">@subhamkrai</a>)</li>
</ul>
