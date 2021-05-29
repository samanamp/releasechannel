# Argocd

<div>
<demo-component app-code="argocd"/>
</div>


## v2.0.3
<p style="font-size:12px;"> 27, May 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v2.0.3" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<div class="highlight highlight-source-shell position-relative"><pre>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.3/manifests/install.yaml</pre></div>
<h4>HA:</h4>
<div class="highlight highlight-source-shell position-relative"><pre>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.3/manifests/ha/install.yaml</pre></div>
<h4>Bug Fixes</h4>
<ul>
<li>fix: add missing --container flag to 'argocd app logs' command (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6320">#6320</a>)</li>
<li>fix: grpc web proxy must ensure to read full header (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6319">#6319</a>)</li>
<li>fix: controller should refresh app before running sync operation (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6294">#6294</a>)</li>
</ul>

## v2.0.2
<p style="font-size:12px;"> 20, May 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v2.0.2" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<div class="highlight highlight-source-shell position-relative"><pre>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.2/manifests/install.yaml</pre></div>
<h4>HA:</h4>
<div class="highlight highlight-source-shell position-relative"><pre>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.2/manifests/ha/install.yaml</pre></div>
<h4>Bug Fixes</h4>
<ul>
<li>fix: enable access to metrics port in embedded network policies (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6277">#6277</a>)</li>
<li>fix: display log streaming error in logs viewer (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/6100">#6100</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6273">#6273</a>)</li>
<li>fix: Don't count errored or completed neighbor pods toward resource consumption (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6259">#6259</a>)</li>
<li>fix: Enable kex algo diffie-hellman-group-exchange-sha256 for go-git ssh (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6256">#6256</a>)</li>
<li>fix: copy github app key from repocreds (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6140">#6140</a>, <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6197">#6197</a>)</li>
<li>fix(ui): UI crashes after reinstalling ArgoCD (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6218">#6218</a>)</li>
<li>fix: add network policies to restrict traffic flow between argocd components (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6156">#6156</a>)</li>
<li>fix: Revert "feat: Add health checks for kubernetes-external-secrets (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5435">#5435</a>)"</li>
<li>chore: Allow ingress traffic to argocd-server by default (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6179">#6179</a>)</li>
</ul>

## stable
<p style="font-size:12px;"> 20, May 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/stable" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Bump version to 2.0.2</p>

## v2.0.1
<p style="font-size:12px;"> 15, Apr 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v2.0.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<div class="highlight highlight-source-shell"><pre>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.1/manifests/install.yaml</pre></div>
<h4>HA:</h4>
<div class="highlight highlight-source-shell"><pre>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.1/manifests/ha/install.yaml</pre></div>
<h4>Bug Fixes</h4>
<ul>
<li>fix: spark application check fails on missing section (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6036">#6036</a>)</li>
<li>fix: Adding explicit bind to redis and sentinel for IPv4 clusters <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5957">#5957</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/6005">#6005</a>)</li>
<li>fix: fix: use correct field for evaluating whether or not GitHub Enterprise is selected (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5987">#5987</a>)</li>
</ul>

## v2.0.0
<p style="font-size:12px;"> 07, Apr 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v2.0.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0/manifests/install.yaml
</code></pre>
<h3>HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0/manifests/ha/install.yaml
</code></pre>
<p><a href="https://blog.argoproj.io/argo-cd-v2-0-rc1-is-here-f7d21ff1aa64" rel="nofollow">2.0 Release blog post</a></p>
<h3>Pods View</h3>
<p>Pods View is particularly useful for applications that have hundreds of pods. Instead of visualizing all Kubernetes<br />
resources for the application, it only shows Kubernetes pods and closely related resources. The Pods View supports<br />
grouping related resources by Parent Resource, Top Level Parent, or by Node. Each way of grouping solves a particular<br />
use case. For example grouping by Top Level Parent allows you to quickly find how many pods your application is running<br />
and which resources created them. Grouping by Node allows to see how Pods are spread across the nodes and how many<br />
resources they requested.</p>
<h3>Logs Viewer</h3>
<p>Argo CD provides a way to see live logs of pods, which is very useful for debugging and troubleshooting. In the v2.0<br />
release, the log visualization has been rewritten to support pagination, filtering, the ability to disable/enable log<br />
streaming, and even a dark mode for terminal lovers. Do you want to see aggregated logs of multiple deployment pods?<br />
Not a problem! Just click on the parent resource such as Deployment, ReplicaSet, or StatefulSet and navigate<br />
to the Logs tab.</p>
<h3>Banner Feature</h3>
<p>Want to notify your Argo CD users of upcoming changes? Just specify the notification message and optional URL using the<br />
<code>ui.bannercontent</code> and <code>ui.bannerurl</code> attributes in the <code>argocd-cm</code> ConfigMap.</p>
<h3>Core Features</h3>
<ul>
<li>The new sync option <code>PrunePropagationPolicy=background</code> allows using background deletion during syncing</li>
<li>New application finalizer <code>resources-finalizer.argocd.argoproj.io:background</code> allows using background deletion when the application is deleted</li>
<li>The new sync option <code>ApplyOutOfSyncOnly=true</code> allows skipping syncing resources that are already in the desired state.</li>
<li>The new sync option <code>PruneLast=true</code> allows deferring resource pruning until the last synchronization phase after all other resources are synced and healthy.</li>
</ul>
<h3>The argocd-util CLI</h3>
<p>Argo CD Util is a CLI tool that contains useful commands for operators who manage Argo CD. Starting from this release<br />
the Argo CD Utility is published with every Argo CD release as a Homebrew installation.</p>
<h3>Features</h3>
<ul>
<li>feat: Add a keyboard shortcut to move focus to search (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4796">#4796</a>)</li>
<li>feat: Add Access-Control-Allow-Origin: * response header to badges (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5395">#5395</a>)</li>
<li>feat: Add additional strimzi custom resource health checks (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5642">#5642</a>)</li>
<li>feat: Add health check for Sealed Secrets (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5503">#5503</a>)</li>
<li>feat: Add health checks for kubernetes-external-secrets (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5435">#5435</a>)</li>
<li>feat: Add resource.Quantity as a known field type for diffing. (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5095">#5095</a>)</li>
<li>feat: add source repos to fields inherited from global projects (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5417">#5417</a>)</li>
<li>feat: added cascade option to delete resources <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5368">#5368</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5538">#5538</a>)</li>
<li>feat: adding noscript tag (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5650">#5650</a>)</li>
<li>feat: Allow GetRevisionMetadata to use truncated sha revision (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5265">#5265</a>)</li>
<li>feat: App list filter counters and labels should dynamically update (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4822">#4822</a>)</li>
<li>feat: Application specific parameter override files (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5038">#5038</a>)</li>
<li>feat: argocd-util can now validate RBAC configuration (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4876">#4876</a>)</li>
<li>feat: Cascade delete option is ticked by default (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/3205">#3205</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4994">#4994</a>)</li>
<li>feat: Clicking on filter bar should expand filter (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5488">#5488</a>)</li>
<li>feat: declarative config for cluster and repo(<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4734">#4734</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5102">#5102</a>)</li>
<li>feat: Display creation time in application node and summary (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4920">#4920</a>)</li>
<li>feat: exposed sync retry options via cli for app create (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5638">#5638</a>)</li>
<li>feat: filter applications by source repo URL (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5602">#5602</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5603">#5603</a>)</li>
<li>feat: Generate declarative config for app and appproj (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4734">#4734</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5014">#5014</a>)</li>
<li>feat: GitHub organization app for git cloning (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4348">#4348</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5355">#5355</a>)</li>
<li>feat: implement 'argocd-util cluster stats' command (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5733">#5733</a>)</li>
<li>feat: implement include filter for directory settings (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5166">#5166</a>)</li>
<li>feat: Include argocd-util as part of release artifacts(<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5174">#5174</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5203">#5203</a>)</li>
<li>feat: list applications filter by name (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4959">#4959</a>)</li>
<li>feat: Logs should favor containers over init containers (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4345">#4345</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5322">#5322</a>)</li>
<li>feat: made Helm v3 the default and removed version auto-detection (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5646">#5646</a>)</li>
<li>feat: prune last <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5080">#5080</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5199">#5199</a>)</li>
<li>feat: regenerate active users token if it is expiring soon (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5629">#5629</a>)</li>
<li>feat: selective sync (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/3877">#3877</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5347">#5347</a>)</li>
<li>feat: set X-XSS-Protection while serving static content (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5412">#5412</a>)</li>
<li>feat: Show number of pod restarts in the argo ui (5041) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5384">#5384</a>)</li>
<li>feat: support add plugin env entry from CLI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4923">#4923</a>)</li>
<li>feat: support background propagation policy while deleting applications (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5216">#5216</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5524">#5524</a>)</li>
<li>feat: support caching helm repo index (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5661">#5661</a>)</li>
<li>feat: support fetch refs (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4893">#4893</a>)</li>
<li>feat: support resource prune propagation policy (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5743">#5743</a>)</li>
<li>feat: support token revocation (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5477">#5477</a>)</li>
<li>feat: support viewing logs of multiple pods in UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5469">#5469</a>)</li>
<li>feat: turn on grpc-web (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5288">#5288</a>)</li>
<li>feat: upgrade kustomize to v3.9.4 and support v3.8.5 breaking change (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5672">#5672</a>)</li>
<li>feat: Upgrade Redis to v6.2.1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5701">#5701</a>)</li>
<li>feat:Issue5408- Increase text contrast for improved web accessibility (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5700">#5700</a>)</li>
<li>feat:Support multibyte for truncate string functions (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5055">#5055</a>)</li>
<li>feat(prom): Add prometheus metrics reset support <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5287">#5287</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5304">#5304</a>)</li>
<li>feat(ui): Filter sync results by status (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5499">#5499</a>)</li>
<li>feat(ui): Filterable pod logs (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5319">#5319</a>)</li>
<li>feat(ui): New pod logs viewer (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5233">#5233</a>)</li>
<li>feat(ui): Open pod logs in an isolated new tab (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5323">#5323</a>)</li>
<li>feat(ui): Pod view (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5091">#5091</a>)</li>
<li>feat(ui): replicaset children of deployment should sort by revision (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4249">#4249</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4252">#4252</a>)</li>
<li>feat(ui): Status panel labels (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5458">#5458</a>)</li>
<li>feat(ui): User defined information banner (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5299">#5299</a>)</li>
<li>feat: add exit-code flag to app diff command (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5852">#5852</a>)</li>
<li>feat: allow per-version kustomize options (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5967">#5967</a>)</li>
</ul>
<h3>Bug Fixes</h3>
<ul>
<li>fix invalid external url (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5396">#5396</a>)</li>
<li>fix: 'argocd app wait --suspended' stuck if operation is in progress (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5511">#5511</a>)</li>
<li>fix: /api/version should not return tools version for unauthenticated requests (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5415">#5415</a>)</li>
<li>fix: a request which was using a revoked project token, would still be allowed to perform requests allowed by default policy (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5378">#5378</a>)</li>
<li>fix: account tokens should be rejected if required capability is disabled (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5414">#5414</a>)</li>
<li>fix: Allow correct SSO redirect URL for CLI static client (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5098">#5098</a>)</li>
<li>fix: API server should not print resource body when resource update fails (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5617">#5617</a>)</li>
<li>fix: app create with -f ignored labels from file (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5268">#5268</a>)</li>
<li>fix: argocd-util import --prune must also remove finalizers if present (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5712">#5712</a>)</li>
<li>fix: autocomplete filter to make it case insensitive <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5152">#5152</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5400">#5400</a>)</li>
<li>fix: Better handling of base64 encoded passwords/credentials (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5023">#5023</a>)</li>
<li>fix: capitalization in headers (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5692">#5692</a>)</li>
<li>fix: Change icons so that there will be no two identical icons together (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4977">#4977</a>)</li>
<li>fix: commit message overflows box (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5043">#5043</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5241">#5241</a>)</li>
<li>fix: Correct Revision History Limit tooltip (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/3534">#3534</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5050">#5050</a>)</li>
<li>fix: correctly sort events by lastTimestamp field (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5383">#5383</a>)</li>
<li>fix: Declarative helm repositories with missing secret causes all repositories in ArgoCD to lock (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/3492">#3492</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5363">#5363</a>)</li>
<li>fix: Design Flaw leading to errant delete (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4844">#4844</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4909">#4909</a>)</li>
<li>fix: directory source include/exclude should match relative file path (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5277">#5277</a>)</li>
<li>fix: don't log certain fields (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5662">#5662</a>)</li>
<li>fix: Dry run stuck on pre sync hook <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5736">#5736</a></li>
<li>fix: Empty resource whitelist allowed all resources (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5540">#5540</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5551">#5551</a>)</li>
<li>fix: Ensure requested file from server is within a base path (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5564">#5564</a>)</li>
<li>fix: Exclude kube-root-ca.crt ConfigMap from Orphaned Resources monitoring by default (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5490">#5490</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5523">#5523</a>)</li>
<li>fix: expand button spacing issue (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5258">#5258</a>)</li>
<li>fix: fix memory leak in application controller (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5604">#5604</a>)</li>
<li>fix: Generate initial admin password in a more secure manner (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5138">#5138</a>)</li>
<li>fix: Handle GnuPG verification errors gracefully (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5560">#5560</a>)</li>
<li>fix: improve 'argocd-util proj generate-spec' usability (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5717">#5717</a>)</li>
<li>fix: Include Headers in login clientopts (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4918">#4918</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4941">#4941</a>)</li>
<li>fix: increase contrast for badge colors (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5678">#5678</a>)</li>
<li>fix: Invalid semantic version MaxVersion (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5740">#5740</a>)  (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5747">#5747</a>)</li>
<li>fix: locale-independent gpg output parsing (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5269">#5269</a>)</li>
<li>fix: Log output fails when JSON logging is enabled (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4911">#4911</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5446">#5446</a>)</li>
<li>fix: Possible nil pointer dereference in repocreds API (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5130">#5130</a>)</li>
<li>fix: Possible nil pointer dereference in repository API (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5128">#5128</a>)</li>
<li>fix: Prevent possible nil pointer dereference in project API (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5263">#5263</a>)</li>
<li>fix: prevent short-circuit during env variable substitution (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4984">#4984</a>)</li>
<li>fix: Prompt for name for managed resources only when deleting (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5033">#5033</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5049">#5049</a>)</li>
<li>fix: Properly escape HTML for error message from CLI SSO (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5563">#5563</a>)</li>
<li>fix: remove invalid assumption about OCI helm chart path (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5179">#5179</a>)</li>
<li>fix: Remove kubectl binary from argo image(<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5005">#5005</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5101">#5101</a>)</li>
<li>fix: return http400/405 to invalid webhook requests (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5565">#5565</a>)</li>
<li>fix: setting 'revision history limit' errors in UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5035">#5035</a>)</li>
<li>fix: show operation status if app is being deleted (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5561">#5561</a>)</li>
<li>fix: support longer http cookie (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/2917">#2917</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5497">#5497</a>)</li>
<li>fix: sync repository certificates UI with other pages(<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4609">#4609</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4971">#4971</a>)</li>
<li>fix: tokens keep working after account is deactivated (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5402">#5402</a>)</li>
<li>fix: updated CRD from apiextensions/v1beta1 to v1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5516">#5516</a>)</li>
<li>fix: updated retry var type from string to duration for app sync (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5583">#5583</a>)</li>
<li>fix: updating cluster drops secret (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5220">#5220</a>)</li>
<li>fix: upgrade klog (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5697">#5697</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5699">#5699</a>)</li>
<li>fix: Use pause icon for Suspended (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4838">#4838</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4905">#4905</a>)</li>
<li>fix: use red spinner for terminating animation (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5252">#5252</a>)</li>
<li>fix(cli): format appURL from server settings (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5333">#5333</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5449">#5449</a>)</li>
<li>fix(ui): Consolidate sync options  (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5357">#5357</a>)</li>
<li>fix(ui): Improve pod view with better space efficiency (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5238">#5238</a>)</li>
<li>fix(ui): improve spacing of app status panel (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5528">#5528</a>)</li>
<li>fix(ui): Only connect edges between resources in the same namespace (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5430">#5430</a>)</li>
<li>fix(ui): out-of-sync button in apps with request hooks (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5625">#5625</a>) Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5125">#5125</a></li>
<li>fix(ui): Overlapping buttons at narrow screen widths (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5259">#5259</a>)</li>
<li>fix(ui): Pod view tooltips positioned incorrectly (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5244">#5244</a>)</li>
<li>fix(ui): Toolbar wrap hides search. Refactor Page (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5593">#5593</a>)</li>
<li>fix(ui): Various minor UI fixes (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5337">#5337</a>)</li>
<li>fix: Presync hooks stop working after namespace resource is added in a Helm chart <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5522">#5522</a></li>
<li>fix: Use helm login for Oci helm repos. <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5856">#5856</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5887">#5887</a>)</li>
<li>fix: fix incorrect OCI Helm registiries assumptions (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5888">#5888</a>)</li>
<li>fix: global project info is missing in UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5861">#5861</a>)</li>
<li>fix: add prefix sync for CLI argocd app flag --retry-limit, --retry-b… (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5876">#5876</a>)</li>
<li>fix: upgrade gitops engine to v0.3.1</li>
<li>fix: non-cascading application delete is broken (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5875">#5875</a>)</li>
<li>fix(ui): Pod logs filter did not refresh on button click. Also add tooltip for clarification (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5858">#5858</a>)</li>
<li>fix: get correct username from jwt token subject (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5836">#5836</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5848">#5848</a>)</li>
<li>fix: application specific parameter override is not reflected in application parameters tab (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5845">#5845</a>)</li>
<li>fix: error when reset application parameters from UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5828">#5828</a>)</li>
<li>fix: support loading oci helm dependencies referenced by chart stored in non-oci repo (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5917">#5917</a>)</li>
<li>fix: Syncing is still slow with ApplyOutOfSyncOnly=true (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5966">#5966</a>)</li>
<li>fix: correct package name in Makefile (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5960">#5960</a>)</li>
</ul>
<h3>Other</h3>
<ul>
<li>chore: build consolidated argocd binary (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5247">#5247</a>)</li>
<li>chore: Change installation manifests to pull images from quay.io (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5227">#5227</a>)</li>
<li>chore: Switch Docker base image to ubuntu:20.10 instead of debian:10-slim (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5185">#5185</a>)</li>
<li>chore: Update Dex to v2.27.0 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5058">#5058</a>)</li>
<li>chore: Upgrade jwt-go to 4.0.0-preview1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5184">#5184</a>)</li>
<li>refactor: applications-list page uses only watch API to quicker show application to the user (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5719">#5719</a>)</li>
<li>refactor: optimize argocd-application-controller redis usage (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5345">#5345</a>)</li>
<li>refactor: restructure 'argocd-util' commands (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5708">#5708</a>)</li>
<li>refactor: upgrade gitops-engine and k8s deps to v0.20.1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5194">#5194</a>)</li>
<li>refactor: upgrade gitops-engine version (closes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4627">#4627</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5235">#5235</a>)</li>
<li>refactor: upgrade helm to 3.5.1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5385">#5385</a>)</li>
<li>chore: Separate "online" mode from "production" mode in yarn build (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5830">#5830</a>)</li>
<li>chore: Fix manifest generation in release and make quay.io the lead (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5831">#5831</a>)</li>
<li>chore: Upgrade Go module to v2 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5931">#5931</a>)</li>
</ul>

## v2.0.0-rc4
<p style="font-size:12px;"> 05, Apr 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v2.0.0-rc4" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0-rc4/manifests/install.yaml
</code></pre>
<h3>HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0-rc4/manifests/ha/install.yaml
</code></pre>
<h3>Bug Fixes</h3>
<ul>
<li>fix: Syncing is still slow with ApplyOutOfSyncOnly=true (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5966">#5966</a>)</li>
<li>fix: correct package name in Makefile (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5960">#5960</a>)</li>
</ul>

## v2.0.0-rc3
<p style="font-size:12px;"> 02, Apr 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v2.0.0-rc3" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0-rc3/manifests/install.yaml
</code></pre>
<h3>HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0-rc3/manifests/ha/install.yaml
</code></pre>
<h3>Bug Fixes</h3>
<ul>
<li>fix: support loading oci helm dependencies referenced by chart stored in non-oci repo (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5917">#5917</a>)</li>
</ul>
<h3>Other</h3>
<ul>
<li>chore: Upgrade Go module to v2 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5931">#5931</a>)</li>
</ul>

## v2.0.0-rc2
<p style="font-size:12px;"> 29, Mar 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v2.0.0-rc2" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0-rc2/manifests/install.yaml
</code></pre>
<h3>HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0-rc2/manifests/ha/install.yaml
</code></pre>
<h3>Features</h3>
<ul>
<li>feat: add exit-code flag to app diff command (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5852">#5852</a>)</li>
</ul>
<h3>Bug Fixes</h3>
<ul>
<li>fix: Use helm login for Oci helm repos. <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5856">#5856</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5887">#5887</a>)</li>
<li>fix: fix incorrect OCI Helm registiries assumptions (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5888">#5888</a>)</li>
<li>fix: global project info is missing in UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5861">#5861</a>)</li>
<li>fix: add prefix sync for CLI argocd app flag --retry-limit, --retry-b… (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5876">#5876</a>)</li>
<li>fix: upgrade gitops engine to v0.3.1</li>
<li>fix: non-cascading application delete is broken (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5875">#5875</a>)</li>
<li>fix(ui): Pod logs filter did not refresh on button click. Also add tooltip for clarification (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5858">#5858</a>)</li>
<li>fix: get correct username from jwt token subject (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5836">#5836</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5848">#5848</a>)</li>
<li>fix: application specific parameter override is not reflected in application parameters tab (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5845">#5845</a>)</li>
<li>fix: error when reset application parameters from UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5828">#5828</a>)</li>
</ul>
<h3>Other</h3>
<ul>
<li>chore: Separate "online" mode from "production" mode in yarn build (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5830">#5830</a>)</li>
<li>chore: Fix manifest generation in release and make quay.io the lead (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5831">#5831</a>)</li>
</ul>

## v2.0.0-rc1
<p style="font-size:12px;"> 19, Mar 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v2.0.0-rc1" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0-rc1/manifests/install.yaml
</code></pre>
<h3>HA:</h3>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.0-rc1/manifests/ha/install.yaml
</code></pre>
<p><a href="https://blog.argoproj.io/argo-cd-v2-0-rc1-is-here-f7d21ff1aa64" rel="nofollow">2.0 Release blog post</a></p>
<h3>Pods View</h3>
<p>Pods View is particularly useful for applications that have hundreds of pods. Instead of visualizing all Kubernetes<br />
resources for the application, it only shows Kubernetes pods and closely related resources. The Pods View supports<br />
grouping related resources by Parent Resource, Top Level Parent, or by Node. Each way of grouping solves a particular<br />
use case. For example grouping by Top Level Parent allows you to quickly find how many pods your application is running<br />
and which resources created them. Grouping by Node allows to see how Pods are spread across the nodes and how many<br />
resources they requested.</p>
<h3>Logs Viewer</h3>
<p>Argo CD provides a way to see live logs of pods, which is very useful for debugging and troubleshooting. In the v2.0<br />
release, the log visualization has been rewritten to support pagination, filtering, the ability to disable/enable log<br />
streaming, and even a dark mode for terminal lovers. Do you want to see aggregated logs of multiple deployment pods?<br />
Not a problem! Just click on the parent resource such as Deployment, ReplicaSet, or StatefulSet and navigate<br />
to the Logs tab.</p>
<h3>Banner Feature</h3>
<p>Want to notify your Argo CD users of upcoming changes? Just specify the notification message and optional URL using the<br />
<code>ui.bannercontent</code> and <code>ui.bannerurl</code> attributes in the <code>argocd-cm</code> ConfigMap.</p>
<h3>Core Features</h3>
<ul>
<li>The new sync option <code>PrunePropagationPolicy=background</code> allows using background deletion during syncing</li>
<li>New application finalizer <code>resources-finalizer.argocd.argoproj.io:background</code> allows using background deletion when the application is deleted</li>
<li>The new sync option <code>ApplyOutOfSyncOnly=true</code> allows skipping syncing resources that are already in the desired state.</li>
<li>The new sync option <code>PruneLast=true</code> allows deferring resource pruning until the last synchronization phase after all other resources are synced and healthy.</li>
</ul>
<h3>The argocd-util CLI</h3>
<p>Argo CD Util is a CLI tool that contains useful commands for operators who manage Argo CD. Starting from this release<br />
the Argo CD Utility is published with every Argo CD release as a Homebrew installation.</p>
<h3>Features</h3>
<ul>
<li>feat: Add a keyboard shortcut to move focus to search (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4796">#4796</a>)</li>
<li>feat: Add Access-Control-Allow-Origin: * response header to badges (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5395">#5395</a>)</li>
<li>feat: Add additional strimzi custom resource health checks (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5642">#5642</a>)</li>
<li>feat: Add health check for Sealed Secrets (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5503">#5503</a>)</li>
<li>feat: Add health checks for kubernetes-external-secrets (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5435">#5435</a>)</li>
<li>feat: Add resource.Quantity as a known field type for diffing. (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5095">#5095</a>)</li>
<li>feat: add source repos to fields inherited from global projects (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5417">#5417</a>)</li>
<li>feat: added cascade option to delete resources <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5368">#5368</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5538">#5538</a>)</li>
<li>feat: adding noscript tag (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5650">#5650</a>)</li>
<li>feat: Allow GetRevisionMetadata to use truncated sha revision (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5265">#5265</a>)</li>
<li>feat: App list filter counters and labels should dynamically update (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4822">#4822</a>)</li>
<li>feat: Application specific parameter override files (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5038">#5038</a>)</li>
<li>feat: argocd-util can now validate RBAC configuration (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4876">#4876</a>)</li>
<li>feat: Cascade delete option is ticked by default (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/3205">#3205</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4994">#4994</a>)</li>
<li>feat: Clicking on filter bar should expand filter (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5488">#5488</a>)</li>
<li>feat: declarative config for cluster and repo(<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4734">#4734</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5102">#5102</a>)</li>
<li>feat: Display creation time in application node and summary (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4920">#4920</a>)</li>
<li>feat: exposed sync retry options via cli for app create (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5638">#5638</a>)</li>
<li>feat: filter applications by source repo URL (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5602">#5602</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5603">#5603</a>)</li>
<li>feat: Generate declarative config for app and appproj (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4734">#4734</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5014">#5014</a>)</li>
<li>feat: GitHub organization app for git cloning (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4348">#4348</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5355">#5355</a>)</li>
<li>feat: implement 'argocd-util cluster stats' command (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5733">#5733</a>)</li>
<li>feat: implement include filter for directory settings (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5166">#5166</a>)</li>
<li>feat: Include argocd-util as part of release artifacts(<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5174">#5174</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5203">#5203</a>)</li>
<li>feat: list applications filter by name (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4959">#4959</a>)</li>
<li>feat: Logs should favor containers over init containers (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4345">#4345</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5322">#5322</a>)</li>
<li>feat: made Helm v3 the default and removed version auto-detection (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5646">#5646</a>)</li>
<li>feat: prune last <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5080">#5080</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5199">#5199</a>)</li>
<li>feat: regenerate active users token if it is expiring soon (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5629">#5629</a>)</li>
<li>feat: selective sync (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/3877">#3877</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5347">#5347</a>)</li>
<li>feat: set X-XSS-Protection while serving static content (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5412">#5412</a>)</li>
<li>feat: Show number of pod restarts in the argo ui (5041) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5384">#5384</a>)</li>
<li>feat: support add plugin env entry from CLI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4923">#4923</a>)</li>
<li>feat: support background propagation policy while deleting applications (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5216">#5216</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5524">#5524</a>)</li>
<li>feat: support caching helm repo index (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5661">#5661</a>)</li>
<li>feat: support fetch refs (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4893">#4893</a>)</li>
<li>feat: support resource prune propagation policy (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5743">#5743</a>)</li>
<li>feat: support token revocation (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5477">#5477</a>)</li>
<li>feat: support viewing logs of multiple pods in UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5469">#5469</a>)</li>
<li>feat: turn on grpc-web (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5288">#5288</a>)</li>
<li>feat: upgrade kustomize to v3.9.4 and support v3.8.5 breaking change (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5672">#5672</a>)</li>
<li>feat: Upgrade Redis to v6.2.1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5701">#5701</a>)</li>
<li>feat:Issue5408- Increase text contrast for improved web accessibility (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5700">#5700</a>)</li>
<li>feat:Support multibyte for truncate string functions (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5055">#5055</a>)</li>
<li>feat(prom): Add prometheus metrics reset support <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5287">#5287</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5304">#5304</a>)</li>
<li>feat(ui): Filter sync results by status (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5499">#5499</a>)</li>
<li>feat(ui): Filterable pod logs (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5319">#5319</a>)</li>
<li>feat(ui): New pod logs viewer (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5233">#5233</a>)</li>
<li>feat(ui): Open pod logs in an isolated new tab (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5323">#5323</a>)</li>
<li>feat(ui): Pod view (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5091">#5091</a>)</li>
<li>feat(ui): replicaset children of deployment should sort by revision (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4249">#4249</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4252">#4252</a>)</li>
<li>feat(ui): Status panel labels (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5458">#5458</a>)</li>
<li>feat(ui): User defined information banner (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5299">#5299</a>)</li>
</ul>
<h3>Bug Fixes</h3>
<ul>
<li>fix invalid external url (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5396">#5396</a>)</li>
<li>fix: 'argocd app wait --suspended' stuck if operation is in progress (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5511">#5511</a>)</li>
<li>fix: /api/version should not return tools version for unauthenticated requests (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5415">#5415</a>)</li>
<li>fix: a request which was using a revoked project token, would still be allowed to perform requests allowed by default policy (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5378">#5378</a>)</li>
<li>fix: account tokens should be rejected if required capability is disabled (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5414">#5414</a>)</li>
<li>fix: Allow correct SSO redirect URL for CLI static client (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5098">#5098</a>)</li>
<li>fix: API server should not print resource body when resource update fails (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5617">#5617</a>)</li>
<li>fix: app create with -f ignored labels from file (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5268">#5268</a>)</li>
<li>fix: argocd-util import --prune must also remove finalizers if present (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5712">#5712</a>)</li>
<li>fix: autocomplete filter to make it case insensitive <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5152">#5152</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5400">#5400</a>)</li>
<li>fix: Better handling of base64 encoded passwords/credentials (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5023">#5023</a>)</li>
<li>fix: capitalization in headers (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5692">#5692</a>)</li>
<li>fix: Change icons so that there will be no two identical icons together (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4977">#4977</a>)</li>
<li>fix: commit message overflows box (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5043">#5043</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5241">#5241</a>)</li>
<li>fix: Correct Revision History Limit tooltip (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/3534">#3534</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5050">#5050</a>)</li>
<li>fix: correctly sort events by lastTimestamp field (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5383">#5383</a>)</li>
<li>fix: Declarative helm repositories with missing secret causes all repositories in ArgoCD to lock (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/3492">#3492</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5363">#5363</a>)</li>
<li>fix: Design Flaw leading to errant delete (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4844">#4844</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4909">#4909</a>)</li>
<li>fix: directory source include/exclude should match relative file path (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5277">#5277</a>)</li>
<li>fix: don't log certain fields (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5662">#5662</a>)</li>
<li>fix: Dry run stuck on pre sync hook <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5736">#5736</a></li>
<li>fix: Empty resource whitelist allowed all resources (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5540">#5540</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5551">#5551</a>)</li>
<li>fix: Ensure requested file from server is within a base path (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5564">#5564</a>)</li>
<li>fix: Exclude kube-root-ca.crt ConfigMap from Orphaned Resources monitoring by default (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5490">#5490</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5523">#5523</a>)</li>
<li>fix: expand button spacing issue (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5258">#5258</a>)</li>
<li>fix: fix memory leak in application controller (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5604">#5604</a>)</li>
<li>fix: Generate initial admin password in a more secure manner (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5138">#5138</a>)</li>
<li>fix: Handle GnuPG verification errors gracefully (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5560">#5560</a>)</li>
<li>fix: improve 'argocd-util proj generate-spec' usability (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5717">#5717</a>)</li>
<li>fix: Include Headers in login clientopts (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4918">#4918</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4941">#4941</a>)</li>
<li>fix: increase contrast for badge colors (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5678">#5678</a>)</li>
<li>fix: Invalid semantic version MaxVersion (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5740">#5740</a>)  (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5747">#5747</a>)</li>
<li>fix: locale-independent gpg output parsing (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5269">#5269</a>)</li>
<li>fix: Log output fails when JSON logging is enabled (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4911">#4911</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5446">#5446</a>)</li>
<li>fix: Possible nil pointer dereference in repocreds API (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5130">#5130</a>)</li>
<li>fix: Possible nil pointer dereference in repository API (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5128">#5128</a>)</li>
<li>fix: Prevent possible nil pointer dereference in project API (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5263">#5263</a>)</li>
<li>fix: prevent short-circuit during env variable substitution (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4984">#4984</a>)</li>
<li>fix: Prompt for name for managed resources only when deleting (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5033">#5033</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5049">#5049</a>)</li>
<li>fix: Properly escape HTML for error message from CLI SSO (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5563">#5563</a>)</li>
<li>fix: remove invalid assumption about OCI helm chart path (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5179">#5179</a>)</li>
<li>fix: Remove kubectl binary from argo image(<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5005">#5005</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5101">#5101</a>)</li>
<li>fix: return http400/405 to invalid webhook requests (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5565">#5565</a>)</li>
<li>fix: setting 'revision history limit' errors in UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5035">#5035</a>)</li>
<li>fix: show operation status if app is being deleted (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5561">#5561</a>)</li>
<li>fix: support longer http cookie (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/2917">#2917</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5497">#5497</a>)</li>
<li>fix: sync repository certificates UI with other pages(<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4609">#4609</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4971">#4971</a>)</li>
<li>fix: tokens keep working after account is deactivated (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5402">#5402</a>)</li>
<li>fix: updated CRD from apiextensions/v1beta1 to v1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5516">#5516</a>)</li>
<li>fix: updated retry var type from string to duration for app sync (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5583">#5583</a>)</li>
<li>fix: updating cluster drops secret (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5220">#5220</a>)</li>
<li>fix: upgrade klog (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5697">#5697</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5699">#5699</a>)</li>
<li>fix: Use pause icon for Suspended (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4838">#4838</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/4905">#4905</a>)</li>
<li>fix: use red spinner for terminating animation (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5252">#5252</a>)</li>
<li>fix(cli): format appURL from server settings (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5333">#5333</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5449">#5449</a>)</li>
<li>fix(ui): Consolidate sync options  (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5357">#5357</a>)</li>
<li>fix(ui): Improve pod view with better space efficiency (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5238">#5238</a>)</li>
<li>fix(ui): improve spacing of app status panel (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5528">#5528</a>)</li>
<li>fix(ui): Only connect edges between resources in the same namespace (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5430">#5430</a>)</li>
<li>fix(ui): out-of-sync button in apps with request hooks (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5625">#5625</a>) Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5125">#5125</a></li>
<li>fix(ui): Overlapping buttons at narrow screen widths (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5259">#5259</a>)</li>
<li>fix(ui): Pod view tooltips positioned incorrectly (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5244">#5244</a>)</li>
<li>fix(ui): Toolbar wrap hides search. Refactor Page (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5593">#5593</a>)</li>
<li>fix(ui): Various minor UI fixes (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5337">#5337</a>)</li>
<li>fix: Presync hooks stop working after namespace resource is added in a Helm chart <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5522">#5522</a></li>
</ul>
<h3>Other</h3>
<ul>
<li>chore: build consolidated argocd binary (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5247">#5247</a>)</li>
<li>chore: Change installation manifests to pull images from quay.io (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5227">#5227</a>)</li>
<li>chore: Switch Docker base image to ubuntu:20.10 instead of debian:10-slim (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5185">#5185</a>)</li>
<li>chore: Update Dex to v2.27.0 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5058">#5058</a>)</li>
<li>chore: Upgrade jwt-go to 4.0.0-preview1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5184">#5184</a>)</li>
<li>refactor: applications-list page uses only watch API to quicker show application to the user (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5719">#5719</a>)</li>
<li>refactor: optimize argocd-application-controller redis usage (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5345">#5345</a>)</li>
<li>refactor: restructure 'argocd-util' commands (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5708">#5708</a>)</li>
<li>refactor: upgrade gitops-engine and k8s deps to v0.20.1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5194">#5194</a>)</li>
<li>refactor: upgrade gitops-engine version (closes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/4627">#4627</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5235">#5235</a>)</li>
<li>refactor: upgrade helm to 3.5.1 (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5385">#5385</a>)</li>
</ul>

## v1.8.7
<p style="font-size:12px;"> 03, Mar 2021 
<a href="https://github.com/argoproj/argo-cd/releases/tag/v1.8.7" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<h3>Non-HA:</h3>
<div class="highlight highlight-source-shell"><pre>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v1.8.7/manifests/install.yaml</pre></div>
<h4>HA:</h4>
<div class="highlight highlight-source-shell"><pre>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v1.8.7/manifests/ha/install.yaml</pre></div>
<h2>Important note</h2>
<p>This release fixed a regression regarding which cluster resources are permitted on the AppProject level. Previous to this fix, after <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/3960">#3960</a> has been merged, all cluster resources were allowed on project level when neither of the allow or deny lists was defined. However, the correct behavior is to block all resources in this case.</p>
<p>If you have Projects with empty allow and deny lists, but want the associated applications be able to sync cluster resources, you will have to adapt your cluster resources allow lists to explicitly allow the resources.</p>
<h4>Bug Fixes</h4>
<ul>
<li>fix: redact sensitive data in logs (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5662">#5662</a>)</li>
<li>fix: Properly escape HTML for error message from CLI SSO (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5563">#5563</a>)</li>
<li>fix: Empty resource whitelist allowed all resources (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/issues/5540">#5540</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-cd/pull/5551">#5551</a>)</li>
</ul>
