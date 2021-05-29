# Argo Rollouts

<div>
<demo-component app-code="argo-rollouts"/>
</div>


## v1.0.1
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v1.0.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quickstart</h2>
<div class="highlight highlight-source-shell position-relative"><pre>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/download/v1.0.1/install.yaml</pre></div>
<h2>Changes since v1.0.1</h2>
<h3>Controller</h3>
<ul>
<li>fix: Modify validation to check Analysis args passed through RO spec (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1215">#1215</a>)</li>
<li>fix: AnalysisRun args could not be resolved from secret (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1213">#1213</a>)</li>
<li>feat: WebMetric to support string body responses (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1212">#1212</a>)</li>
</ul>

## v1.0.0
<p style="font-size:12px;"> 20, May 2021 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v1.0.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quickstart</h2>
<div class="snippet-clipboard-content position-relative"><pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/download/v1.0.0/install.yaml
</code></pre></div>
<h2>Notable Features</h2>
<ul>
<li>New Argo Rollouts UI available in <code>kubectl argo rollouts dashboard</code></li>
<li>Ability to reference existing Deployment workloads instead of inlining a PodTemplate at spec.template</li>
<li>Richer Prometheus stats and Kubernetes events</li>
<li>Support for Ambassador as a canary traffic router</li>
<li>Support canarying using Istio DestinationRule subsets</li>
</ul>
<h2>Upgrade Notes</h2>
<h3>Installation Manifests</h3>
<p>Installation manifests are now attached as GitHub Release artifacts (as opposed to raw files checked into git)<br />
and can be installed with the release download URL. e.g.:</p>
<div class="snippet-clipboard-content position-relative"><pre><code>kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/download/v1.0.0/install.yaml
</code></pre></div>
<h3>Argo CD OutOfSync status on Rollout v1.0.0 CRDs:</h3>
<p>Argo Rollouts v1.0 now vends apiextensions.k8s.io/v1 CustomResourceDefinitions (previously apiextensions.k8s.io/v1beta1). Kubernetes v1 CRDs no longer supports the preservation of unknown fields in objects, and rejects attempts to set <code>spec.preserveUnknownFields: true</code> (the previous default). In order to support a smooth upgrade from Argo Rollouts v0.10 to v1.0, <code>spec.preserveUnknownFields</code> is explicitly set to <code>false</code> in the manifests, despite <code>false</code> being the default, and only option in v1 CRDs. However this causes diffing tools (such as Argo CD) to report the manifest as OutOfSync (since K8s drops the false field).</p>
<p>More information:</p>
<ul>
<li><a class="issue-link js-issue-link" href="https://github.com/kubernetes-sigs/controller-tools/issues/476">kubernetes-sigs/controller-tools#476</a></li>
<li><a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1069">#1069</a></li>
</ul>
<p>To avoid the Argo CD OutOfSync conditions, you can remove <code>spec.preserveUnknownFields</code> from the manifests<br />
entirely <em>after upgrading to v1.0</em>.</p>
<p>Alternatively, you can instruct Argo CD to ignore differences using ignoreDifferences in the Application spec:</p>
<div class="highlight highlight-source-yaml position-relative"><pre><span class="pl-ent">spec</span>:
  <span class="pl-ent">ignoreDifferences</span>:
  - <span class="pl-ent">group</span>: <span class="pl-s">apiextensions.k8s.io</span>
    <span class="pl-ent">kind</span>: <span class="pl-s">CustomResourceDefinition</span>
    <span class="pl-ent">jsonPointers</span>:
    - <span class="pl-s">/spec/preserveUnknownFields</span></pre></div>
<h3>Deprecation of <code>kubectl argo rollouts promote --skip-current-step</code> flag</h3>
<p>The promote flag <code>--skip-current-step</code> which skips the current running canary step has been deprecated and will be removed in a future release. Its logic to skipping the current step has been merged with the existing command:</p>
<div class="highlight highlight-source-shell position-relative"><pre>kubectl argo rollouts promote ROLLOUT</pre></div>
<p>The <code>promote ROLLOUT</code> command can now be used to handle both the case where the rollout needs to be unpaused, as well as to skip the currently running canary step (e.g. an analysis/experiment/pause step).</p>
<h2>Changes since v0.10</h2>
<h3>Controller</h3>
<ul>
<li>feat: support reference model for workloads (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/676">#676</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1072">#1072</a>)</li>
<li>feat: Implement Ambassador to be used as traffic router for canary deployments (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1025">#1025</a>)</li>
<li>feat: support canarying using Istio DestinationRule subsets (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/985">#985</a>)</li>
<li>feat: istio virtualservice and rollout in different namespaces</li>
<li>feat: add ability to verify canary weights before advancing steps (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/957">#957</a>)</li>
<li>feat: support scaleDownDelaySeconds in canary w/ traffic routing (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1056">#1056</a>)</li>
<li>feat: Add ability to restart maxUnavailable pods to BlueGreen strategy (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/937">#937</a>)</li>
<li>feat(controller): Add support for ephemeral metadata on BlueGreen rollouts. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/973">#973</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/974">#974</a>)</li>
<li>feat: Allow user to handle NaN result in Analysis (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/977">#977</a>)</li>
<li>feat: Wait for canary RS to have ready replicas before shifting labels (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1022">#1022</a>)</li>
<li>feat: Create RolloutPaused condition (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1054">#1054</a>)</li>
<li>feat: Add RolloutCompleted condition (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1074">#1074</a>)</li>
<li>feat: add print version flag to rollouts-controller</li>
<li>feat: calculate rollout phase &amp; message controller side</li>
<li>fix: Fixes the regression of dropping resources from argo-rollouts crds. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/1043">#1043</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1044">#1044</a>)</li>
<li>fix: Set Canary Strategy default maxUnavailable to 25% (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/981">#981</a>)</li>
<li>fix: blue-green rollouts could pause prematurely during prePromotionAnalysis (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1007">#1007</a>)</li>
<li>fix: Clear ProgressDeadlineExceeded Condition in paused BlueGreen Rollout (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1002">#1002</a>)</li>
<li>fix: analysis template arguments validate (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1038">#1038</a>)</li>
<li>fix: calculate scale down count. (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1047">#1047</a>)</li>
<li>fix: verify analysis arguments name with those in the rollout (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1071">#1071</a>)</li>
<li>fix: rollout status always in progressing if analysis fails (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1099">#1099</a>)</li>
<li>fix: Add edge case handling to traffic routing (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1190">#1190</a>)</li>
<li>fix: unhandled error patchVirtualService (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1168">#1168</a>)</li>
<li>fix: handling error on f.close (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1167">#1167</a>)</li>
<li>fix: rollouts in middle of restart should be considered Progressing</li>
</ul>
<h3>Analysis</h3>
<ul>
<li>feat: metric fields can be parameterized by analysis arguments (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/901">#901</a>)</li>
<li>feat: support a custom base URL for the new relic provider (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1053">#1053</a>)</li>
<li>feat: Allow Datadog API and APP keys to be consumed from env vars (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1073">#1073</a>)</li>
<li>fix: Improve validation for AnalysisTemplates referenced by RO (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1094">#1094</a>)</li>
<li>fix: wavefront queries would return no datapoints. surface evaluate errors</li>
<li>fix: metrics which errored did not retry at error interval</li>
<li>fix: Improve and refactor validation for AnalysisTemplates</li>
</ul>
<h3>Plugin</h3>
<ul>
<li>feat: Argo Rollouts api-server and UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1015">#1015</a>)</li>
<li>feat: Implement rollout status command. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/596">#596</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1001">#1001</a>)</li>
<li>feat: lint supporting rollout in multiple doc</li>
<li>fix: get rollout always return not found except default namespace (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/961">#961</a>)</li>
<li>fix: create command not support namespace in yaml file (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/962">#962</a>)</li>
<li>fix: kubectl argo create panic: runtime error: invalid memory address or nil pointer dereference</li>
</ul>
<h3>Misc</h3>
<ul>
<li>chore: publish plugin image automatically. migrate to quay.io (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1102">#1102</a>)</li>
<li>feat: support ARM builds, remove unused components in Dockerfile (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/889">#889</a>)</li>
<li>chore: update k8s dependencies to v1.20. improve logging (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/994">#994</a>)</li>
<li>fix: add informational exposed ports to deployment (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1066">#1066</a>)</li>
<li>chore: Outsource reusable UI components to argo-ux npm package</li>
<li>fix: use fixed size int32</li>
</ul>

## v1.0.0-rc1
<p style="font-size:12px;"> 05, May 2021 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v1.0.0-rc1" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quickstart</h2>
<pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/download/v1.0.0-rc1/install.yaml
</code></pre>
<h2>Notable Features</h2>
<ul>
<li><a href="https://argoproj.github.io/argo-rollouts/dashboard/" rel="nofollow">New Argo Rollouts UI available</a> in <code>kubectl argo rollouts dashboard</code></li>
<li><a href="https://argoproj.github.io/argo-rollouts/migrating/#reference-deployment-from-rollout" rel="nofollow">Ability to reference existing Deployment workloads</a> instead of inlining a PodTemplate at spec.template</li>
<li><a href="https://argoproj.github.io/argo-rollouts/features/traffic-management/ambassador/" rel="nofollow">Support for Ambassador as a canary traffic router</a></li>
<li><a href="https://argoproj.github.io/argo-rollouts/features/traffic-management/istio/#subset-level-traffic-splitting" rel="nofollow">Support canarying using Istio DestinationRule subsets</a></li>
</ul>
<h2>Upgrade Notes</h2>
<h3>Installation Manifests</h3>
<p>Installation manifests are now attached as GitHub Release artifacts (as opposed to raw files checked into git)<br />
and can be installed with the release download URL. e.g.:</p>
<pre><code>kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/download/v1.0.0-rc1/install.yaml
</code></pre>
<h3>Argo CD OutOfSync status on Rollout v1.0.0 CRDs:</h3>
<p>Argo Rollouts v1.0 now vends apiextensions.k8s.io/v1 CustomResourceDefinitions (previously apiextensions.k8s.io/v1beta1).<br />
Kubernetes v1 CRDs no longer supports the preservation of unknown fields in objects, and rejects<br />
attempts to set <code>spec.preserveUnknownFields: true</code>. In order to support a smooth upgrade from<br />
Argo Rollouts v0.10 to v1.0, <code>spec.preserveUnknownFields</code> is explicitly set to <code>false</code> in the manifests,<br />
despite <code>false</code> being the default, and only option in v1 CRDs. However this causes diffing tools<br />
(such as Argo CD) to report the manifest as OutOfSync (since K8s drops the false field).</p>
<p>More information:</p>
<ul>
<li><a class="issue-link js-issue-link" href="https://github.com/kubernetes-sigs/controller-tools/issues/476">kubernetes-sigs/controller-tools#476</a></li>
<li><a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1069">#1069</a></li>
</ul>
<p>To avoid the Argo CD OutOfSync conditions, you can remove <code>spec.preserveUnknownFields</code> from the manifests<br />
entirely <em>after upgrading from v0.10</em>.</p>
<p>Alternatively, you can instruct Argo CD to ignore differences using <code>ignoreDifferences</code> in the Application spec:</p>
<div class="highlight highlight-source-yaml"><pre><span class="pl-ent">spec</span>:
  <span class="pl-ent">ignoreDifferences</span>:
  - <span class="pl-ent">group</span>: <span class="pl-s">apiextensions.k8s.io</span>
    <span class="pl-ent">kind</span>: <span class="pl-s">CustomResourceDefinition</span>
    <span class="pl-ent">jsonPointers</span>:
    - <span class="pl-s">/spec/preserveUnknownFields</span></pre></div>
<h2>Changes since v0.10</h2>
<h3>Controller</h3>
<ul>
<li>feat: support reference model for workloads (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/676">#676</a>) (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1072">#1072</a>)</li>
<li>feat: Implement Ambassador to be used as traffic router for canary deployments (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1025">#1025</a>)</li>
<li>feat: support canarying using Istio DestinationRule subsets (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/985">#985</a>)</li>
<li>feat: istio virtualservice and rollout in different namespaces</li>
<li>feat: add ability to verify canary weights before advancing steps (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/957">#957</a>)</li>
<li>feat: support scaleDownDelaySeconds in canary w/ traffic routing (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1056">#1056</a>)</li>
<li>feat: Add ability to restart maxUnavailable pods to BlueGreen strategy (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/937">#937</a>)</li>
<li>feat(controller): Add support for ephemeral metadata on BlueGreen rollouts. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/973">#973</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/974">#974</a>)</li>
<li>feat: Allow user to handle NaN result in Analysis (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/977">#977</a>)</li>
<li>feat: Wait for canary RS to have ready replicas before shifting labels (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1022">#1022</a>)</li>
<li>feat: Create RolloutPaused condition (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1054">#1054</a>)</li>
<li>feat: Add RolloutCompleted condition (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1074">#1074</a>)</li>
<li>fix: Fixes the regression of dropping resources from argo-rollouts crds. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/1043">#1043</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1044">#1044</a>)</li>
<li>fix: Set Canary Strategy default maxUnavailable to 25% (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/981">#981</a>)</li>
<li>fix: blue-green rollouts could pause prematurely during prePromotionAnalysis (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1007">#1007</a>)</li>
<li>fix: Clear ProgressDeadlineExceeded Condition in paused BlueGreen Rollout (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1002">#1002</a>)</li>
<li>fix: analysis template arguments validate (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1038">#1038</a>)</li>
<li>fix: calculate scale down count. (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1047">#1047</a>)</li>
<li>fix: verify analysis arguments name with those in the rollout (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1071">#1071</a>)</li>
<li>fix: rollout status always in progressing if analysis fails (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1099">#1099</a>)</li>
</ul>
<h3>Analysis</h3>
<ul>
<li>feat: metric fields can be parameterized by analysis arguments (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/901">#901</a>)</li>
<li>feat: support a custom base URL for the new relic provider (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1053">#1053</a>)</li>
<li>feat: Allow Datadog API and APP keys to be consumed from env vars (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1073">#1073</a>)</li>
<li>fix: Improve validation for AnalysisTemplates referenced by RO (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1094">#1094</a>)</li>
<li>fix: wavefront queries would return no datapoints. surface evaluate errors</li>
<li>fix: metrics which errored did not retry at error interval</li>
</ul>
<h3>Plugin</h3>
<ul>
<li>feat: Argo Rollouts api-server and UI (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1015">#1015</a>)</li>
<li>feat: Implement rollout status command. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/596">#596</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1001">#1001</a>)</li>
<li>fix: get rollout always return not found except default namespace (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/961">#961</a>)</li>
<li>fix: create command not support namespace in yaml file (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/962">#962</a>)</li>
<li>fix: kubectl argo create panic: runtime error: invalid memory address or nil pointer dereference</li>
</ul>
<h3>Misc</h3>
<ul>
<li>chore: publish plugin image automatically. migrate to quay.io (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1102">#1102</a>)</li>
<li>feat: support ARM builds, remove unused components in Dockerfile (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/889">#889</a>)</li>
<li>chore: update k8s dependencies to v1.20. improve logging (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/994">#994</a>)</li>
<li>fix: add informational exposed ports to deployment (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/1066">#1066</a>)</li>
</ul>

## v0.10.2
<p style="font-size:12px;"> 17, Dec 2020 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v0.10.2" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://raw.githubusercontent.com/argoproj/argo-rollouts/v0.10.2/manifests/install.yaml
</code></pre>
<h2>Changes since v0.10.1</h2>
<h3>Controller</h3>
<ul>
<li>fix: switch pod restart to use evict API to honor PDBs</li>
<li>fix: ephemeral metadata injection was dropping metadata injected by mutating webhooks</li>
<li>fix: requiredForCompletion did not work for an experiment started by a rollout</li>
<li>fix: Add missing RoleBinding file to namespace installation</li>
</ul>

## stable: chore: update install manifests to v0.10.2
<p style="font-size:12px;"> 17, Dec 2020 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/stable" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Signed-off-by: Jesse Suen <a href="mailto:jesse_suen@intuit.com">jesse_suen@intuit.com</a></p>

## v0.10.1
<p style="font-size:12px;"> 05, Dec 2020 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v0.10.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>v0.10.1</h1>
<h2>Quick Start</h2>
<pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://raw.githubusercontent.com/argoproj/argo-rollouts/v0.10.1/manifests/install.yaml
</code></pre>
<h2>Changes since v0.10.0</h2>
<h3>Controller</h3>
<ul>
<li>fix: restart was restarting too many pods when available &gt; spec.replicas (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/856">#856</a>)</li>
<li>fix: Correct Istio VirtualService immediately when not in desired state (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/874">#874</a>)</li>
</ul>
<h3>Plugin</h3>
<ul>
<li>fix: plugin incorrectly treated v0.9 rollout as v0.10 when it had numeric observedGeneration (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/875">#875</a>)</li>
</ul>

## v0.10.0
<p style="font-size:12px;"> 14, Nov 2020 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v0.10.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h1>v0.10.0</h1>
<h2>Quick Start</h2>
<pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://raw.githubusercontent.com/argoproj/argo-rollouts/v0.10.0/manifests/install.yaml
</code></pre>
<h2>Notable Features</h2>
<ul>
<li>Ability to set canary vs. stable ephemeral metadata on rollout Pods during an update</li>
<li>Support new metric providers: New Relic, Datadog</li>
<li>Ability to control canary scale during an update</li>
<li>Ability to restart up to maxUnavailable pods at a time for a canary rollout</li>
<li>Ability to self reference rollout metadata as arguments to analysis</li>
<li>Ability to fully promote blue-green and canary rollouts (skipping steps, analysis, pauses)</li>
<li>kubectl-argo-rollouts plugin command to lint rollout</li>
<li>kubectl-argo-rollouts plugin command to undo a rollout (same as kubectl rollout undo)</li>
</ul>
<h2>Upgrade Notes</h2>
<p>Rollouts v0.10 has switched to using Kubernetes <a href="https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#status-subresource" rel="nofollow">CRD Status Subresources</a> (<a href="https://github.com/argoproj/argo-rollouts/pull/789">PR #789</a>). This feature allows the rollout controller to record the numeric <code>metadata.generation</code> into <code>status.observedGeneration</code> which provides a reliable indicator of a Rollout who's spec has (or has not yet) been observed by the controller (for example if the argo-rollouts controller was down or delayed).</p>
<p>A consequence of this change, is that the v0.10 rollout controller should be used with the v0.10 kubectl-argo-rollouts plugin in order to perform actions such as abort, pause, promote. Similarly, Argo CD v1.8 should be with the v0.10 rollout controller when performing those same actions. Both kubectl-argo-rollouts plugin v0.10 and Argo CD v1.8 are backwards compatible with v0.9 rollouts controller.</p>
<h2>Changes since v0.9</h2>
<h3>Controller</h3>
<ul>
<li>feat: set canary/stable ephemeral metadata to pods during updates (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/770">#770</a>)</li>
<li>feat: add support for valueFrom in analysis arguments. (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/797">#797</a>)</li>
<li>feat: Adding rollout_info_replicas_desired metric. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/748">#748</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/749">#749</a>)</li>
<li>feat: restart pods up to maxUnavailable at a time</li>
<li>feat: add full rollout promotion (skip analysis, pause, steps)</li>
<li>feat: use CRD status subresource (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/789">#789</a>)</li>
<li>feat: Allow setting canary weight without side-effects. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/556">#556</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/677">#677</a>)</li>
<li>fix: namespaced scoped controller support (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/818">#818</a>)</li>
<li>fix: fetch secrets on-demand to fix controller boot for large clusters (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/829">#829</a>)</li>
</ul>
<h3>Analysis</h3>
<ul>
<li>feat: Add New Relic metricprovider (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/772">#772</a>)</li>
<li>feat: Add Datadog metric provider. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/702">#702</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/705">#705</a>)</li>
</ul>
<h3>Plugin</h3>
<ul>
<li>feat: Implement kubectl argo rollouts lint</li>
<li>feat: Add undo command in kubectl plugin. Fixes <a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/issues/575">#575</a> (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/812">#812</a>)</li>
<li>fix: kubectl plugin should use dynamic client</li>
</ul>
<h3>Misc</h3>
<ul>
<li>fix: rollout kustomize transform analysis ref should use templateName instead of name (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/809">#809</a>)</li>
<li>fix: add missing Service kustomize name reference in trafficRouting/alb/rootService (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/699">#699</a>)</li>
</ul>

## v0.9.3
<p style="font-size:12px;"> 05, Nov 2020 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v0.9.3" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://raw.githubusercontent.com/argoproj/argo-rollouts/v0.9.3/manifests/install.yaml
</code></pre>
<h2>Changes since v0.9.2</h2>
<h2>Controller</h2>
<ul>
<li>fix: scaleDownDelayRevisionLimit was off by one (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/816">#816</a>)</li>
<li>fix: background analysis refs were not verified. requeue InvalidSpec rollouts (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/814">#814</a>)</li>
<li>fix(controller): fix unhandled panic from malformed rollout (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/801">#801</a>)</li>
<li>fix(controller): validation should not consider privileged security context (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/802">#802</a>)</li>
</ul>

## v0.9.2
<p style="font-size:12px;"> 17, Oct 2020 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v0.9.2" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://raw.githubusercontent.com/argoproj/argo-rollouts/v0.9.2/manifests/install.yaml
</code></pre>
<h2>Changes since v0.9.1</h2>
<h2>Controller</h2>
<ul>
<li>fix(controller): controller did not honor maxUnavailable during rollback (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/786">#786</a>)</li>
<li>fix(controller): blue-green with analysis was broken (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/780">#780</a>)</li>
<li>fix(controller): blue-green fast-tracked rollbacks would still start analysis templates</li>
<li>fix(controller): prePromotionAnalysis with previewReplicaCount would pause indefinitely w/o running analysis</li>
<li>fix(controller): calculate available replicas from active ReplicaSet (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/757">#757</a>)</li>
</ul>
<h2>Plugin</h2>
<ul>
<li>feat(plugin): indicate the stable ReplicaSet for blue-green rollouts in plugin</li>
<li>feat(plugin): plugin now surfaces InvalidSpec errors and failed analysisrun messages (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/729">#729</a>)</li>
<li>fix(plugin): bluegreen scaleDownDelay was delaying Healthy status. Present errors in message field (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/768">#768</a>)</li>
</ul>

## v0.9.1
<p style="font-size:12px;"> 29, Sep 2020 
<a href="https://github.com/argoproj/argo-rollouts/releases/tag/v0.9.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Quick Start</h2>
<pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://raw.githubusercontent.com/argoproj/argo-rollouts/v0.9.1/manifests/install.yaml
</code></pre>
<h2>Changes since v0.9.0</h2>
<h3>General</h3>
<ul>
<li>feat: writeback rollout updates to informer to prevent stale data (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/726">#726</a>)</li>
<li>fix: unavailable stable RS was not scaled down to make room for canary (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/739">#739</a>)</li>
<li>fix: make controllers tolerant to spec marshalling errors (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/666">#666</a>)</li>
<li>perf: Create IstioVirtualServiceLister (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/656">#656</a>)</li>
<li>fix: add missing log message when a controller's syncHandler returns error (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/658">#658</a>)</li>
<li>fix: support azure auth (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/664">#664</a>)</li>
</ul>
<h3>Analysis</h3>
<ul>
<li>feat: web metrics preserve data types, allow insecure tls, and make jsonPath optional (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/731">#731</a>)</li>
<li>fix: analysis controller could get into a hotloop with terminated run (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/724">#724</a>)</li>
<li>fix: do not create analysisruns with initial deploy (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/722">#722</a>)</li>
<li>fix: add Failed AnalysisRun phase status to analysis_run_metric_phase and analysis_run_phase metrics. (<a class="issue-link js-issue-link" href="https://github.com/argoproj/argo-rollouts/pull/618">#618</a>)</li>
</ul>
