# etcd

<div>
<demo-component app-code="etcd"/>
</div>


## v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/v3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Please check out <a href="https://github.com/etcd-io/etcd/blob/master/CHANGELOG-3.5.md">CHANGELOG</a> for a full list of changes. And make sure to read <a href="https://github.com/etcd-io/website/blob/main/content/en/docs/next/upgrades/upgrade_3_5.md">upgrade guide</a> before upgrading etcd (there may be breaking changes).</p>
<p>For installation guides, please check out <a href="http://play.etcd.io" rel="nofollow">play.etcd.io</a> and <a href="https://github.com/etcd-io/etcd/tree/master/Documentation#operating-etcd-clusters">operating etcd</a>. Latest support status for common architectures and operating systems can be found at <a href="https://github.com/etcd-io/website/blob/main/content/en/docs/next/op-guide/supported-platform.md">supported platforms</a>.</p>
<h6>Linux</h6>
<div class="highlight highlight-source-shell position-relative"><pre>ETCD_VER=v3.5.0-beta.4

<span class="pl-c"><span class="pl-c">#</span> choose either URL</span>
GOOGLE_URL=https://storage.googleapis.com/etcd
GITHUB_URL=https://github.com/etcd-io/etcd/releases/download
DOWNLOAD_URL=<span class="pl-smi">${GOOGLE_URL}</span>

rm -f /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-linux-amd64.tar.gz
rm -rf /tmp/etcd-download-test <span class="pl-k">&amp;&amp;</span> mkdir -p /tmp/etcd-download-test

curl -L <span class="pl-smi">${DOWNLOAD_URL}</span>/<span class="pl-smi">${ETCD_VER}</span>/etcd-<span class="pl-smi">${ETCD_VER}</span>-linux-amd64.tar.gz -o /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-linux-amd64.tar.gz
tar xzvf /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-linux-amd64.tar.gz -C /tmp/etcd-download-test --strip-components=1
rm -f /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-linux-amd64.tar.gz

/tmp/etcd-download-test/etcd --version
/tmp/etcd-download-test/etcdctl version
/tmp/etcd-download-test/etcdutl version</pre></div>
<div class="highlight highlight-source-shell position-relative"><pre><span class="pl-c"><span class="pl-c">#</span> start a local etcd server</span>
/tmp/etcd-download-test/etcd

<span class="pl-c"><span class="pl-c">#</span> write,read to etcd</span>
/tmp/etcd-download-test/etcdctl --endpoints=localhost:2379 put foo bar
/tmp/etcd-download-test/etcdctl --endpoints=localhost:2379 get foo</pre></div>
<h6>macOS (Darwin)</h6>
<div class="highlight highlight-source-shell position-relative"><pre>ETCD_VER=v3.5.0-beta.4

<span class="pl-c"><span class="pl-c">#</span> choose either URL</span>
GOOGLE_URL=https://storage.googleapis.com/etcd
GITHUB_URL=https://github.com/etcd-io/etcd/releases/download
DOWNLOAD_URL=<span class="pl-smi">${GOOGLE_URL}</span>

rm -f /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-darwin-amd64.zip
rm -rf /tmp/etcd-download-test <span class="pl-k">&amp;&amp;</span> mkdir -p /tmp/etcd-download-test

curl -L <span class="pl-smi">${DOWNLOAD_URL}</span>/<span class="pl-smi">${ETCD_VER}</span>/etcd-<span class="pl-smi">${ETCD_VER}</span>-darwin-amd64.zip -o /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-darwin-amd64.zip
unzip /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-darwin-amd64.zip -d /tmp <span class="pl-k">&amp;&amp;</span> rm -f /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-darwin-amd64.zip
mv /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-darwin-amd64/<span class="pl-k">*</span> /tmp/etcd-download-test <span class="pl-k">&amp;&amp;</span> rm -rf mv /tmp/etcd-<span class="pl-smi">${ETCD_VER}</span>-darwin-amd64

/tmp/etcd-download-test/etcd --version
/tmp/etcd-download-test/etcdctl version
/tmp/etcd-download-test/etcdutl version</pre></div>
<h6>Docker</h6>
<p>etcd uses <a href="https://gcr.io/etcd-development/etcd" rel="nofollow"><code>gcr.io/etcd-development/etcd</code></a> as a primary container registry, and <a href="https://quay.io/coreos/etcd" rel="nofollow"><code>quay.io/coreos/etcd</code></a> as secondary.</p>
<div class="highlight highlight-source-shell position-relative"><pre>rm -rf /tmp/etcd-data.tmp <span class="pl-k">&amp;&amp;</span> mkdir -p /tmp/etcd-data.tmp <span class="pl-k">&amp;&amp;</span> \
  docker rmi gcr.io/etcd-development/etcd:v3.5.0-beta.4 <span class="pl-k">||</span> <span class="pl-c1">true</span> <span class="pl-k">&amp;&amp;</span> \
  docker run \
  -p 2379:2379 \
  -p 2380:2380 \
  --mount type=bind,source=/tmp/etcd-data.tmp,destination=/etcd-data \
  --name etcd-gcr-v3.5.0-beta.4 \
  gcr.io/etcd-development/etcd:v3.5.0-beta.4 \
  /usr/local/bin/etcd \
  --name s1 \
  --data-dir /etcd-data \
  --listen-client-urls http://0.0.0.0:2379 \
  --advertise-client-urls http://0.0.0.0:2379 \
  --listen-peer-urls http://0.0.0.0:2380 \
  --initial-advertise-peer-urls http://0.0.0.0:2380 \
  --initial-cluster s1=http://0.0.0.0:2380 \
  --initial-cluster-token tkn \
  --initial-cluster-state new \
  --log-level info \
  --logger zap \
  --log-outputs stderr

docker <span class="pl-c1">exec</span> etcd-gcr-v3.5.0-beta.4 /bin/sh -c <span class="pl-s"><span class="pl-pds">"</span>/usr/local/bin/etcd --version<span class="pl-pds">"</span></span>
docker <span class="pl-c1">exec</span> etcd-gcr-v3.5.0-beta.4 /bin/sh -c <span class="pl-s"><span class="pl-pds">"</span>/usr/local/bin/etcdctl version<span class="pl-pds">"</span></span>
docker <span class="pl-c1">exec</span> etcd-gcr-v3.5.0-beta.4 /bin/sh -c <span class="pl-s"><span class="pl-pds">"</span>/usr/local/bin/etcdctl endpoint health<span class="pl-pds">"</span></span>
docker <span class="pl-c1">exec</span> etcd-gcr-v3.5.0-beta.4 /bin/sh -c <span class="pl-s"><span class="pl-pds">"</span>/usr/local/bin/etcdctl put foo bar<span class="pl-pds">"</span></span>
docker <span class="pl-c1">exec</span> etcd-gcr-v3.5.0-beta.4 /bin/sh -c <span class="pl-s"><span class="pl-pds">"</span>/usr/local/bin/etcdctl get foo<span class="pl-pds">"</span></span>
docker <span class="pl-c1">exec</span> etcd-gcr-v3.5.0-beta.4 /bin/sh -c <span class="pl-s"><span class="pl-pds">"</span>/usr/local/bin/etcdutl version<span class="pl-pds">"</span></span></pre></div>

## tests/v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/tests%2Fv3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v3.5.0-beta.4</p>

## server/v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/server%2Fv3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v3.5.0-beta.4</p>

## raft/v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/raft%2Fv3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v3.5.0-beta.4</p>

## pkg/v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/pkg%2Fv3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v3.5.0-beta.4</p>

## etcdutl/v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/etcdutl%2Fv3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v3.5.0-beta.4</p>

## etcdctl/v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/etcdctl%2Fv3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v3.5.0-beta.4</p>

## client/v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/client%2Fv3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v3.5.0-beta.4</p>

## client/v2.305.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/client%2Fv2.305.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v2.305.0-beta.4</p>

## client/pkg/v3.5.0-beta.4
<p style="font-size:12px;"> 26, May 2021 
<a href="https://github.com/etcd-io/etcd/releases/tag/client%2Fpkg%2Fv3.5.0-beta.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>v3.5.0-beta.4</p>
