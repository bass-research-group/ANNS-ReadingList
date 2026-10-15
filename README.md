# ANNS-ReadingList

A paper reading list for vector search and ANNS. 
We read papers from [system conferences](https://nebelwelt.net/pubstats/top-authors-sys.html) like [ISCA](https://iscaconf.org/), [VLDB](https://www.vldb.org/), [SIGMOD](https://sigmod.org/), [MICRO](https://microarch.org/), [ASPLOS](https://www.asplos-conference.org/), [HPCA](https://hpca-conf.org/), [OSDI, SOSP](https://www.usenix.org/conferences), [SC](https://supercomputing.org/), [PPoPP](https://ppopp25.sigplan.org/), [MLSys](https://mlsys.org/).

A few must-reads to get started on ANNS research:

1. [FAISS GPU](https://arxiv.org/pdf/1702.08734.pdf)
2. [HNSW](https://arxiv.org/ftp/arxiv/papers/1603/1603.09320.pdf) 
3. [DiskANN](https://proceedings.neurips.cc/paper_files/paper/2019/file/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Paper.pdf) [[Video](https://www.microsoft.com/en-us/research/video/research-talk-approximate-nearest-neighbor-search-systems-at-scale/)] [[Slides](https://cvpr.thecvf.com/media/cvpr-2023/Slides/18545_SzZdLZD.pdf)] [[Slides2](https://people.csail.mit.edu/jshun/6506-s24/lectures/lecture21-2.pdf)] 
4. [RaBitQ](https://dl.acm.org/doi/pdf/10.1145/3654970). [SIGMOD 2024]
5. [SymphonyQG](https://dl.acm.org/doi/10.1145/3709730) [SIGMOD 2025]
6. [ParlayANN](https://arxiv.org/pdf/2305.04359.pdf), [PPoPP 2024]
7. [CAGRA](https://arxiv.org/pdf/2308.15136.pdf), [ICDE 2024]
8. [BigFANN](https://chenxuhao.github.io/docs/vldb-2026.pdf), [VLDB 2026]

## How this list is organized

**Scope.** Approximate nearest neighbor search (ANNS) and vector search papers at
SOSP, OSDI, ASPLOS, SIGMOD, VLDB, MLSys, ISCA, MICRO, HPCA, SC and PPoPP, **from 2025 on**.
RAG and KV-cache papers are included only when vector retrieval is the core of the paper.

**Sub-topics.** Every paper has exactly one:

| Group | Sub-topic | What goes there |
|---|---|---|
| Algorithms | ANNS Indexing Algorithms | Graph, IVF/clustering, tree and hashing indexes; quantization; search, early termination, updates, tuning, theory |
| | Filtered ANNS Algorithms | Vector search under attribute, label, range or other predicates |
| | Hybrid Search Algorithms | Vectors combined with other modalities: multi-vector, dense + sparse/keyword, cross-modal |
| Systems | GPU-Accelerated ANNS Systems | Vector search on GPUs, including CPU-GPU co-processing |
| | Out-of-Core ANNS Systems | Indexes beyond DRAM: SSD/disk-resident, tiered or disaggregated memory |
| | Distributed ANNS Systems | Multi-node, RDMA, federated and scale-out search |
| | Vector Databases & Other Systems | Vector DBMSs and DBMS integration, CPU engines, privacy/security, retrieval for RAG and KV caches |
| Architecture | FPGA & In-storage Acceleration | FPGAs and processing inside storage devices (computational SSDs, in-flash/NAND) |
| | Domain-specific Accelerators | Dedicated hardware only: ASICs and processing-in/near-memory (PIM/NDP). GPU work is under Systems |
| Experiments & Analysis | Benchmarks | Benchmark suites and experimental evaluations comparing existing methods ([Experiments & Analysis] papers) |
| | Workload Characterization | In-depth analyses of time/I/O/memory behavior, design-space explorations, characterization on specific hardware |
| | Surveys | Surveys and tutorials |

**Views.** The list below is grouped by sub-topic, then by venue and year. [`papers/by-venue/`](papers/by-venue/) has one page per
conference. The README covers the most recent years (`readme_years` in [`config.yaml`](config.yaml)); older years move to
[`archive/`](archive/) automatically.

**Links.** `[paper]` is the official publication, `[pdf]` a free PDF, `[arXiv]` the preprint, and `[code]` the authors' code
or artifact, where one exists.

**Markers.** *(accepted, to appear)*: the paper is known only from the program or the authors' own statement, not yet from DBLP.
*(auto-added, not yet reviewed)*: the monthly updater added it and a person has not checked its sub-topic yet.

## Coverage notes (last checked 2026-10-15)

- **Checked against DBLP**: SOSP, OSDI, ASPLOS, SIGMOD, VLDB, MLSys 2025–2026; HPCA 2025–2026; SC 2025; PPoPP 2025–2026.
- **Checked from the official programs**: ISCA 2025–2026, MICRO 2025, MICRO 2026 (to appear; some author lists are partial).
- **Partial**: SC 2026, SIGMOD 2027 and VLDB 2027 (from authors' announcements), late PVLDB vol 19 issues. The official
  [SIGMOD 2027 accepted-papers page](https://2027.sigmod.org/sigmod_papers.shtml) could not be read from the environment
  this list was built in; the monthly updater reads it.
- **Not decided yet**: ASPLOS 2027 (no vector-search paper among early acceptances), HPCA 2027, PPoPP 2027, MLSys 2027.
- SOSP 2025–2026 and ASPLOS 2026 have no paper whose core is vector search.

## Automatic updates

[`.github/workflows/update.yml`](.github/workflows/update.yml) runs on the 2nd of every month (and on demand from the Actions tab):

1. [`scripts/update.py`](scripts/update.py) pulls accepted-paper lists from DBLP (through
   [csconf-papers](https://github.com/RealZST/csconf-papers) and the DBLP SPARQL endpoint), reads official accepted-paper pages
   listed under `official` in `config.yaml` (currently [SIGMOD's](https://2027.sigmod.org/sigmod_papers.shtml)), and searches
   arXiv for preprints whose comments say they were accepted to one of the venues.
   - Papers already listed get missing links filled in. A paper marked *accepted* gets its official link once DBLP has it, and loses the mark.
   - New papers whose titles clearly match (`keywords.strong` in `config.yaml`) are added with a guessed sub-topic and marked *auto-added*.
   - Weaker matches go to [`data/candidates.md`](data/candidates.md) for a person to accept or dismiss.
   - Papers with an arXiv preprint but no code link get one if the arXiv abstract or comments point to GitHub/GitLab.
2. [`scripts/build.py`](scripts/build.py) re-renders this README, the per-venue pages and the archive.
3. The result is committed; if fetching failed, an issue is opened.

The updater never deletes a paper.

## Editing the list

All content lives in [`data/papers/<year>.yaml`](data/papers/). To review auto-added papers, fix `category`/`tags` and delete
`auto: true`. To dismiss a candidate for good, add its title to [`data/excluded.txt`](data/excluded.txt). Then run

```sh
pip install -r requirements.txt
python3 scripts/build.py    # re-render README.md, papers/by-venue/, archive/
python3 -m pytest -q        # offline checks of the data and scripts
python3 scripts/update.py   # optional: fetch new papers now (needs network access)
```

Pushing changes under `data/` to `main` also re-renders the pages automatically.

## Paper list

<!-- BEGIN GENERATED -->
**165** papers from 2025 on.

| Venue | 2025 | 2026 | 2027 | Total |
|---|---|---|---|---|
| [SOSP](papers/by-venue/SOSP.md) | — | — | — | 0 |
| [OSDI](papers/by-venue/OSDI.md) | 3 | 2 | — | 5 |
| [ASPLOS](papers/by-venue/ASPLOS.md) | 1 | — | — | 1 |
| [SIGMOD](papers/by-venue/SIGMOD.md) | 16 | 43 | 12 | 71 |
| [VLDB](papers/by-venue/VLDB.md) | 26 | 33 | 5 | 64 |
| [MLSys](papers/by-venue/MLSys.md) | — | 3 | — | 3 |
| [ISCA](papers/by-venue/ISCA.md) | 7 | 1 | — | 8 |
| [MICRO](papers/by-venue/MICRO.md) | 2 | 4 | — | 6 |
| [HPCA](papers/by-venue/HPCA.md) | 2 | 1 | — | 3 |
| [SC](papers/by-venue/SC.md) | 2 | 1 | — | 3 |
| [PPoPP](papers/by-venue/PPoPP.md) | 1 | — | — | 1 |

| Sub-topic | 2025 | 2026 | 2027 | Total |
|---|---|---|---|---|
| [Algorithms: ANNS Indexing Algorithms](#anns-indexing-algorithms) | 15 | 28 | 6 | 49 |
| [Algorithms: Filtered ANNS Algorithms](#filtered-anns-algorithms) | 8 | 10 | 3 | 21 |
| [Algorithms: Hybrid Search Algorithms](#hybrid-search-algorithms) | 1 | 1 | 1 | 3 |
| [Systems: GPU-Accelerated ANNS Systems](#gpu-accelerated-anns-systems) | 0 | 12 | 1 | 13 |
| [Systems: Out-of-Core ANNS Systems](#out-of-core-anns-systems) | 3 | 4 | 0 | 7 |
| [Systems: Distributed ANNS Systems](#distributed-anns-systems) | 4 | 4 | 1 | 9 |
| [Systems: Vector Databases & Other Systems](#vector-databases--other-systems) | 12 | 9 | 4 | 25 |
| [Architecture: FPGA & In-storage Acceleration](#fpga--in-storage-acceleration) | 4 | 3 | 0 | 7 |
| [Architecture: Domain-specific Accelerators](#domain-specific-accelerators) | 9 | 3 | 0 | 12 |
| [Experiments & Analysis: Benchmarks](#benchmarks) | 2 | 9 | 1 | 12 |
| [Experiments & Analysis: Workload Characterization](#workload-characterization) | 1 | 4 | 0 | 5 |
| [Experiments & Analysis: Surveys](#surveys) | 1 | 1 | 0 | 2 |

### Algorithms

#### ANNS Indexing Algorithms

_Graph, IVF/clustering, tree and hashing indexes; quantization; search, early termination, updates, tuning and theory._


**SIGMOD 2027**

- **Amora: Communication-Efficient Private Approximate Nearest Neighbors Search** *(accepted, to appear)*<br>Qiuhao Wang, Zuowei Chen, Xu Yang, Saiyu Qi, Yong Qi [[code]](https://github.com/meander-wqh/Amora) `privacy`<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>
- **Exploiting Structural Properties for Efficient Constraint-Aware HNSW Hyperparameter Tuning** *(accepted, to appear)*<br>Geon Choi, Hoeun Lee, Jaeyoung Do [[arXiv]](https://arxiv.org/abs/2607.04630) [[code]](https://github.com/AIDASLab/CHAT) `graph` `tuning`<br><sub>SIGMOD 2027 round 1 (official accepted-papers page).</sub>
- **Hardware-Optimized Quantized Graphs for Fast Similarity Search** *(accepted, to appear)*<br>Xiao Luo, John Paparrizos `graph` `quantization`<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>
- **RaP: A Redirect-and-Patch Framework for Efficient Dynamic Updates in Graph-Based ANN Indexes** *(accepted, to appear)*<br>Zhoujin Tian, Xi Zhao, Yao Tian, Zhengjun Huang, Xiaofang Zhou `graph` `dynamic`<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>
- **Reverse Neighbor Sliding and Order Selection for Efficient Multi-Proximity Graph Merging** *(accepted, to appear)*<br>Liuchang Jing, Mingyu Yang, Lei Li, Jianbin Qin, Wei Wang [[arXiv]](https://arxiv.org/abs/2602.17099) [[code]](https://github.com/JingLiuchang/hnsw-merge) `graph` `merging`<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>

**VLDB 2027**

- **HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search** *(accepted, to appear)*<br>Fahong Zhang, Weijie Jin, Lixu Wang, et al. `privacy` `mpc` `graph`

**SIGMOD 2026**

- **Accelerating High-Dimensional ANN Search via Skipping Redundant Distance Computations**<br>Ziwen Song, Bin Wang, Xiaochun Yang [[paper]](https://doi.org/10.1145/3769753)
- **DARTH: Declarative Recall Through Early Termination for Approximate Nearest Neighbor Search**<br>Manos Chatzakis, Yannis Papakonstantinou, Themis Palpanas [[paper]](https://doi.org/10.1145/3749160) [[arXiv]](https://arxiv.org/abs/2505.19001) [[code]](https://github.com/MChatzakis/DARTH) `early-termination`
- **Distribution-Aware Exploration for Adaptive HNSW Search**<br>Chao Zhang, Renée J. Miller [[paper]](https://doi.org/10.1145/3786639) [[arXiv]](https://arxiv.org/abs/2512.06636) [[code]](https://github.com/chaozhang-cs/hnsw-ada-ef) `graph`
- **Dynamically Detect and Fix Hardness for Efficient Approximate Nearest Neighbor Search**<br>Zhiyuan Hua, Qiji Mo, Zebin Yao, Lixiao Cui, Xiaoguang Liu, Gang Wang, et al. [[paper]](https://doi.org/10.1145/3769783) [[code]](https://github.com/yuhuifishash/NGFix) `graph`
- **Efficient and Robust Out-Of-Distribution Vector Similarity Search with Cross-Distribution Monotonic Graph**<br>Qiang Yue, Mengzhao Wang, Xiaoliang Xu, Cheng Long, Yuxiang Wang, Jiahui Wang [[paper]](https://doi.org/10.1145/3786643) [[code]](https://github.com/Lsyhprum/CDMG) `graph` `ood`
- **Efficient Approximate Nearest Neighbor Search via Hemi-Sphere Centroids Graph**<br>Runwen Qiu, Jing Tang [[paper]](https://doi.org/10.1145/3769786) [[code]](https://github.com/QiuRunwen/hscg) `graph`
- **Efficient Vector Index Merging in Vector Databases**<br>Chenzhe Jin, Yunan Zhang, Jiayi Liu, Jianguo Wang [[paper]](https://doi.org/10.1145/3786645) `merging`
- **Enhancing Graph-based Approximate Maximum Inner Product Search via Norm-Adaptive Partitioning**<br>Xi Zhao, Zhoujin Tian, Kai Huang, Yao Tian, Xiaokui Xiao, Bolong Zheng, et al. [[paper]](https://doi.org/10.1145/3802051) `mips` `graph`
- **Fast-Convergent Proximity Graphs for Approximate Nearest Neighbor Search**<br>Binhong Li, Xiao Yan, Shangqi Lu [[paper]](https://doi.org/10.1145/3786650) [[arXiv]](https://arxiv.org/abs/2510.05975) [[code]](https://github.com/Binglbh/Fast-Convergent-Proximity-Graphs-for-Approximate-Nearest-Neighbor-Search) `graph`
- **FGIM: a Fast Graph-based Indexes Merging Framework for Approximate Nearest Neighbor Search**<br>Zekai Wu, Jiabao Jin, Peng Cheng, Xiaoyao Zhong, Lei Chen, Yongxin Tong, et al. [[paper]](https://doi.org/10.1145/3786651) [[arXiv]](https://arxiv.org/abs/2603.21710) `graph` `merging`
- **LM-Tree: A Hybrid Learned Index for Similarity Search in Metric Spaces**<br>Yaqi Wang, Bin Wang, Rui Zhu, Wenli Sun, Xiaochun Yang [[paper]](https://doi.org/10.1145/3786665) `metric-space` `learned`
- **On Efficient Approximate Aggregate Nearest Neighbor Queries over Learned Representations**<br>Carrie Wang, Sihem Amer-Yahia, Laks V. S. Lakshmanan, Reynold Cheng [[paper]](https://doi.org/10.1145/3786672) [[arXiv]](https://arxiv.org/abs/2502.18803) [[code]](https://github.com/Carrieww/AQNNs)
- **PGTuner: An Efficient Framework for Automatic and Transferable Configuration Tuning of Proximity Graphs**<br>Hao Duan, Yitong Song, Bin Yao, Anqi Liang [[paper]](https://doi.org/10.1145/3749179) [[arXiv]](https://arxiv.org/abs/2508.17886) [[code]](https://github.com/hao-duan/PGTuner) `graph` `tuning`
- **RAIRS: Optimizing Redundant Assignment and List Layout for IVF-Based ANN Search**<br>Zehai Yang, Shimin Chen [[paper]](https://doi.org/10.1145/3786687) [[arXiv]](https://arxiv.org/abs/2601.07183) [[code]](https://github.com/schencoding/rairs) `ivf`
- **SAQ: Pushing the Limits of Vector Quantization through Code Adjustment and Dimension Segmentation**<br>Hui Li, Shiyuan Deng, Xiao Yan, Xiangyu Zhi, James Cheng [[paper]](https://doi.org/10.1145/3769824) [[arXiv]](https://arxiv.org/abs/2509.12086) [[code]](https://github.com/howarlii/SAQ) `quantization`
- **TaCo: Data-adaptive and Query-aware Subspace Collision for High-dimensional Approximate Nearest Neighbor Search**<br>Jiuqi Wei, Zhenyu Liao, Ruoyu Han, Quanqing Xu, Chuanhui Yang, Themis Palpanas [[paper]](https://doi.org/10.1145/3802118) [[arXiv]](https://arxiv.org/abs/2603.24919) [[code]](https://github.com/WeiJiuQi/TaCo)
- **TRIM: Accelerating High-Dimensional Vector Similarity Search with Enhanced Triangle-Inequality-Based Pruning**<br>Yitong Song, Pengcheng Zhang, Chao Gao, Bin Yao, Kai Wang, Zongyuan Wu, et al. [[paper]](https://doi.org/10.1145/3769838) [[code]](https://github.com/petrizhang/TRIM)

**VLDB 2026**

- **A Topology-Aware Localized Update Strategy for Graph-Based ANN Index**<br>Song Yu, Shengyuan Lin, Shufeng Gong, Yongqing Xie, Ruicheng Liu, Yijie Zhou, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p495-yu.pdf) [[code]](https://github.com/iDC-NEU/Greator) `graph` `dynamic`
- **ANNiE: A Learned Query Cost Estimator for Graph-Based Approximate Nearest Neighbor Search**<br>Zeyu Wang, Manos Chatzakis, Qitong Wang, Themis Palpanas, Peng Wang, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p3820-wang.pdf) [[code]](https://github.com/CaucherWang/ANNiE) `graph` `cost-model`
- **BBC: Improving Large-𝑘 Approximate Nearest Neighbor Search with a Bucket-based Result Collector**<br>Ziqi Yin, Gao Cong, Kai Zeng, Jinwei Zhu, Bin Cui [[paper]](https://www.vldb.org/pvldb/vol19/p3468-yin.pdf) [[code]](https://github.com/Heisenberg-Yin/BBC) `large-k`
- **ConANN: Conformal Approximate Nearest Neighbor Search**<br>Sonia Horchidan, Fabian Zeiher, Henrik Boström, Paris Carbone [[paper]](https://www.vldb.org/pvldb/vol19/p29-horchidan.pdf) [[code]](https://github.com/soniahorchidan/conann)
- **CONDA: A Connectivity-Aware Dynamic Index for Approximate Nearest Neighbor Search over Evolving Data**<br>Darae Lee, Min-Soo Kim [[paper]](https://www.vldb.org/pvldb/vol19/p3357-lee.pdf) [[code]](https://github.com/darae-lee/CONDA) `dynamic` `graph`
- **HEXA: A Disjoint-Subgraph-Based Indexing Framework for Approximate Nearest Neighbor Search at Billion Scale**<br>Yifei Xu, Yanyan Shen, Youmin Chen, Linpeng Huang [[paper]](https://www.vldb.org/pvldb/vol19/p2922-shen.pdf) `graph` `billion-scale`
- **JHQ: Johnson-Lindenstrauss Enhanced Hierarchical Quantization for High-Dimensional Approximate Nearest Neighbor Search**<br>Jiabao Han, Mengxuan Zhang, Goce Trajcevski [[paper]](https://www.vldb.org/pvldb/vol19/p1530-han.pdf) [[code]](https://github.com/ANU-DB-Mengxuan-Group/VLDB26-JHQ) `quantization`
- **QBAT: Model-based Query Budget Autotuner for Clustering-based Approximate Nearest Neighbor Search**<br>Jonghyun Bae, Tae Jun Ham, Alan Li, Supawit Chockchowwat, Yannis Papakonstantinou [[paper]](https://www.vldb.org/pvldb/vol19/p3091-chockchowwat.pdf) `ivf` `tuning`
- **Quantization Meets Projection: A Happy Marriage for Approximate k-Nearest Neighbor Search**<br>Mingyu Yang, Liuchang Jing, Wentao Li, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p1240-yang.pdf) [[code]](https://github.com/mingyu-hkustgz/RESQ) `quantization`
- **Sparse Neighborhood Graph-Based Approximate Nearest Neighbor Search Revisited: Theoretical Analysis and Optimization**<br>Xinran Ma, Zhaoqi Zhou, Chuan Zhou, Zaijiu Shang, Guoliang Li, Zhiming Ma [[paper]](https://www.vldb.org/pvldb/vol19/p2817-zhou.pdf) [[code]](https://github.com/maxila320/OPT-SNG) `graph` `theory`

**MLSys 2026**

- **When Enough is Enough: Rank-Aware Early Termination for Vector Search**<br>Jianan Lu, Asaf Cidon, Michael Freedman [[paper]](https://proceedings.mlsys.org/paper_files/paper/2026/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html) [[pdf]](https://proceedings.mlsys.org/paper_files/paper/2026/file/78834433edc3291f4c6cbbd2759324db-Paper-Conference.pdf) `early-termination`

**SIGMOD 2025**

- **Fast Approximate Similarity Join in Vector Databases**<br>Jiadong Xie, Jeffrey Xu Yu, Yingfan Liu [[paper]](https://doi.org/10.1145/3725403) `join`
- **MIRAGE-ANNS: Mixed Approach Graph-based Indexing for Approximate Nearest Neighbor Search**<br>Sairaj Voruganti, M. Tamer Özsu [[paper]](https://doi.org/10.1145/3725325) `graph`
- **Practical and Asymptotically Optimal Quantization of High-Dimensional Vectors in Euclidean Space for Approximate Nearest Neighbor Search**<br>Jianyang Gao, Yutong Gou, Yuexuan Xu, Yongyi Yang, Cheng Long, Raymond Chi-Wing Wong [[paper]](https://doi.org/10.1145/3725413) [[arXiv]](https://arxiv.org/abs/2409.09913) [[code]](https://github.com/VectorDB-NTU/Extended-RaBitQ) `quantization`
- **Subspace Collision: An Efficient and Accurate Framework for High-dimensional Approximate Nearest Neighbor Search**<br>Jiuqi Wei, Xiaodong Lee, Zhenyu Liao, Themis Palpanas, Botao Peng [[paper]](https://doi.org/10.1145/3709729) [[arXiv]](https://arxiv.org/abs/2411.14754) [[code]](https://github.com/WeiJiuQi/SuCo)
- **SymphonyQG: Towards Symphonious Integration of Quantization and Graph for Approximate Nearest Neighbor Search**<br>Yutong Gou, Jianyang Gao, Yuexuan Xu, Cheng Long [[paper]](https://doi.org/10.1145/3709730) [[arXiv]](https://arxiv.org/abs/2411.12229) [[code]](https://github.com/gouyt13/SymphonyQG) `graph` `quantization`

**VLDB 2025**

- **Accelerating Approximate Nearest Neighbor Search in Hierarchical Graphs: Efficient Level Navigation with Shortcuts**<br>Zengyang Gong, Yuxiang Zeng, Lei Chen [[paper]](https://www.vldb.org/pvldb/vol18/p3518-chen.pdf) `graph`
- **Cardinality Estimation for Similarity Search on High-Dimensional Data Objects: The Impact of Reference Objects**<br>Hai Lan, Shixun Huang, Zhifeng Bao, Renata Borovica-Gajic [[paper]](https://www.vldb.org/pvldb/vol18/p544-bao.pdf) [[code]](https://github.com/rmitbggroup/CE4HD)
- **Cracking Vector Search Indexes**<br>Vasilis Mageirakos, Bowen Wu, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p3951-mageirakos.pdf) [[code]](https://github.com/mageirakos/crack-ivf-vldb) `adaptive`
- **Efficient Data-aware Distance Comparison Operations for High-Dimensional Approximate Nearest Neighbor Search**<br>Liwei Deng, Penghao Chen, Ximu Zeng, Tianfu Wang, Yan Zhao, Kai Zheng [[paper]](https://www.vldb.org/pvldb/vol18/p812-zheng.pdf) [[code]](https://github.com/Ur-Eine/DADE)
- **GTI: Graph-based Tree Index with Logarithm Updates for Nearest Neighbor Search in High-Dimensional Spaces**<br>Ruiyao Ma, Yifan Zhu, Baihua Zheng, Lu Chen, Congcong Ge, Yunjun Gao [[paper]](https://www.vldb.org/pvldb/vol18/p986-gao.pdf) [[code]](https://github.com/ZJU-DAILY/GTI-Graph-based-Tree-Index) `dynamic`
- **Maximum Inner Product is Query-Scaled Nearest Neighbor**<br>Tingyang Chen, Cong Fu, Kun Wang, Xiangyu Ke, Yunjun Gao, Wenchao Zhou, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p1770-ke.pdf) [[code]](https://github.com/ZJU-DAILY/PSP) `mips`
- **Not Small Enough? SegPQ: A Learned Approach to Compress Product Quantization Codebooks**<br>Qiyu Liu, Yanlin Qi, Siyuan Han, Jingshu Peng, Jin Li, Lei Chen [[paper]](https://www.vldb.org/pvldb/vol18/p3730-liu.pdf) [[code]](https://github.com/qyliu-hkust/segpq) `quantization`
- **Revisiting the Index Construction of Proximity Graph-Based Approximate Nearest Neighbor Search**<br>Shuo Yang, Jiadong Xie, Yingfan Liu, Jeffrey Xu Yu, Xiyue Gao, Qianru Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p1825-liu.pdf) [[code]](https://github.com/xdyangsh/FastKCNA) `graph`
- **Wolverine: Highly Efficient Monotonic Search Path Repair for Graph-based ANN Index Updates**<br>Dawei Liu, Bolong Zheng, Ziyang Yue, Fuhao Ruan, Xiaofang Zhou, Christian S. Jensen [[paper]](https://www.vldb.org/pvldb/vol18/p2268-zheng.pdf) [[code]](https://github.com/LDW2020/Wolverine) `graph` `dynamic`

**PPoPP 2025**

- **PANNS: Enhancing Graph-based Approximate Nearest Neighbor Search through Recency-aware Construction and Parameterized Search**<br>Xizhe Yin, Chao Gao, Zhijia Zhao, et al. [[paper]](https://doi.org/10.1145/3710848.3710867) `graph`

#### Filtered ANNS Algorithms

_Vector search under attribute, label, range or other structured predicates._


**SIGMOD 2027**

- **Dynamic Graph Indexing for Label-Filtered Approximate Nearest Neighbor Search** *(accepted, to appear)*<br>Mengxu Jiang, Zhi Yang, Fangyuan Zhang, Yin Yang, Sibo Wang `dynamic` `graph`<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>
- **Fast Label-Filtering Approximate Nearest Neighbor Search via Progressive Label Set Stratification** *(accepted, to appear)*<br>Ziqi Wang, Jingzhe Zhang, Shuo Shen, Wei Hu [[arXiv]](https://arxiv.org/abs/2609.15058)<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>

**VLDB 2027**

- **VectorMaton: Efficient Vector Search with Pattern Constraints via an Enhanced Suffix Automaton** *(accepted, to appear)*<br>Haoxuan Xie, Siqiang Luo [[arXiv]](https://arxiv.org/abs/2603.01525) [[code]](https://github.com/ForwardStar/VectorMaton)

**SIGMOD 2026**

- **Beyond Vector Search: Querying With and Without Predicates**<br>Jiadong Xie, Jeffrey Xu Yu, Siyi Teng, Yingfan Liu [[paper]](https://doi.org/10.1145/3769765)
- **Curator: Efficient Vector Search with Low-Selectivity Filters**<br>Yicheng Jin, Yongji Wu, Wenjun Hu, Bruce M. Maggs, Jun Yang, Xiao Zhang, et al. [[paper]](https://doi.org/10.1145/3786635) [[arXiv]](https://arxiv.org/abs/2601.01291) [[code]](https://github.com/hatsu3/curator-v2)
- **FAVOR: Efficient Filter-Agnostic Vector ANNS Based on Selectivity-Aware Exclusion Distances**<br>Junjie Song, Yu Liu, Guoyu Hu, Zhongle Xie, Ming Yang, Beng Chin Ooi, et al. [[paper]](https://doi.org/10.1145/3802060) [[arXiv]](https://arxiv.org/abs/2605.07770)
- **PathSeer: Adaptive Neighbor Handling for Efficient Filtered ANN Search**<br>Zhiyue Li, Guangyan Zhang, Ruochun Jin, Bojun Li, Xiaoguang Ren, Wenjing Yang [[paper]](https://doi.org/10.1145/3802098) [[code]](https://github.com/lizhiyuell/PathSeer)
- **WoW: A Window-to-Window Incremental Index for Range-Filtering Approximate Nearest Neighbor Search**<br>Ziqi Wang, Jingzhe Zhang, Wei Hu [[paper]](https://doi.org/10.1145/3769843) [[arXiv]](https://arxiv.org/abs/2508.18617) [[code]](https://github.com/nju-websoft/WoW)

**VLDB 2026**

- **CGIF: Combining Proximity Graphs and Inverted Files for Efficient Filtered Vector Search over Arbitrary Predicates**<br>Jiarui Luo, Chaoji Zuo, Dong Deng [[paper]](https://www.vldb.org/pvldb/vol19/p3663-luo.pdf) [[code]](https://github.com/rutgers-db/CGIF)
- **Elastic Index Selection for Label-Hybrid AKNN Search**<br>Mingyu Yang, Wenxuan Xia, Wentao Li, Raymond Chi-Wing Wong, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p617-yang.pdf) [[code]](https://github.com/mingyu-hkustgz/LabelANN)
- **GAS: A Lightweight Framework for Filtered Search over Wide-table Vectors**<br>Ziyuan He, Yuxiang Wang, Yu Sun, Zijie Ma, Hui Li, Qian Tao, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p3133-tong.pdf)
- **Harmonizing Efficiency and Accuracy in Filtered Vector Search**<br>Zixiang Zhou, Xuhao Chen [[paper]](https://www.vldb.org/pvldb/vol19/p2059-chen.pdf) [[code]](https://github.com/zhouzixiang2004/BigFANN)<br><sub>The BigFANN paper.</sub>
- **RNSG: A Range-Aware Graph Index for Efficient Range-Filtered Approximate Nearest Neighbor Search**<br>Zhiqiu Zou, Ziqi Yin, Rong-Hua Li, Hongchao Qin, Qiangqiang Dai, Guoren Wang [[paper]](https://www.vldb.org/pvldb/vol19/p2839-zou.pdf) [[code]](https://github.com/fallleaves01/R-NSG)

**SIGMOD 2025**

- **DIGRA: A Dynamic Graph Indexing for Approximate Nearest Neighbor Search with Range Filter**<br>Mengxu Jiang, Zhi Yang, Fangyuan Zhang, Guanhao Hou, Jieming Shi, Wenchao Zhou, et al. [[paper]](https://doi.org/10.1145/3725399) [[code]](https://github.com/CUHK-DBGroup/DIGRA) `dynamic`
- **Efficient Dynamic Indexing for Range Filtered Approximate Nearest Neighbor Search**<br>Fangyuan Zhang, Mengxu Jiang, Guanhao Hou, Jieming Shi, Hua Fan, Wenchao Zhou, et al. [[paper]](https://doi.org/10.1145/3725401) [[code]](https://github.com/CUHK-DBGroup/RangePQ) `dynamic`
- **iRangeGraph: Improvising Range-dedicated Graphs for Range-filtering Nearest Neighbor Search**<br>Yuexuan Xu, Jianyang Gao, Yutong Gou, Cheng Long, Christian S. Jensen [[paper]](https://doi.org/10.1145/3698814) [[arXiv]](https://arxiv.org/abs/2409.02571) [[code]](https://github.com/YuexuanXu7/iRangeGraph)
- **Navigating Labels and Vectors: A Unified Approach to Filtered Approximate Nearest Neighbor Search**<br>Yuzheng Cai, Jiayang Shi, Yizhuo Chen, Weiguo Zheng [[paper]](https://doi.org/10.1145/3698822) [[code]](https://github.com/YZ-Cai/Unified-Navigating-Graph)
- **RWalks: Random Walks as Attribute Diffusers for Filtered Vector Search**<br>Anas Ait Aomar, Karima Echihabi, Marco Arnaboldi, Ioannis Alagiannis, Damien Hilloulin, Manal Cherkaoui [[paper]](https://doi.org/10.1145/3725349) [[code]](https://github.com/AnasAito/rwalks-reproduce-v2)

**VLDB 2025**

- **Dynamic Range-Filtering Approximate Nearest Neighbor Search**<br>Zhencan Peng, Miao Qiao, Wenchao Zhou, Feifei Li, Dong Deng [[paper]](https://www.vldb.org/pvldb/vol18/p3256-deng.pdf) [[code]](https://github.com/rutgers-db/DynamicSegmentGraph) `dynamic`
- **SIEVE: Effective Filtered Vector Search with Collection of Indexes**<br>Zhaoheng Li, Silu Huang, Wei Ding, Yongjoo Park, Jianjun Chen [[paper]](https://www.vldb.org/pvldb/vol18/p4723-li.pdf) [[code]](https://github.com/BillyZhaohengLi/SIEVE-vldb25)
- **UNIFY: Unified Index for Range Filtered Approximate Nearest Neighbors Search**<br>Anqi Liang, Pengcheng Zhang, Bin Yao, Zhongpu Chen, Yitong Song, Guangxu Cheng [[paper]](https://www.vldb.org/pvldb/vol18/p1118-yao.pdf) [[code]](https://github.com/sjtu-dbgroup/UNIFY)

#### Hybrid Search Algorithms

_Search that combines vectors with other modalities or representations, such as multi-vector, dense + sparse/keyword, and cross-modal retrieval._


**VLDB 2027**

- **CORAL: Cross-modal Vector Retrieval via Incremental Graph Construction at Scale** *(accepted, to appear)*<br>Shixin Wan, Guoyu Hu, Yifan Wu, et al. [[arXiv]](https://arxiv.org/abs/2610.11230) `graph` `cross-modal` `dynamic`

**SIGMOD 2026**

- **GEM: A Native Graph-based Index for Multi-Vector Retrieval**<br>Yao Tian, Zhoujin Tian, Xi Zhao, Ruiyuan Zhang, Xiaofang Zhou [[paper]](https://doi.org/10.1145/3802065) [[arXiv]](https://arxiv.org/abs/2603.20336) `multi-vector` `graph`

**SIGMOD 2025**

- **DEG: Efficient Hybrid Vector Search Using the Dynamic Edge Navigation Graph**<br>Ziqi Yin, Jianyang Gao, Pasquale Balsebre, Gao Cong, Cheng Long [[paper]](https://doi.org/10.1145/3709679) [[arXiv]](https://arxiv.org/abs/2502.07343) [[code]](https://github.com/Heisenberg-Yin/DEG) `hybrid` `graph`

### Systems

#### GPU-Accelerated ANNS Systems

_Vector search systems built on GPUs, including CPU-GPU co-processing._


**SIGMOD 2027**

- **All-in-One Graph-Based Indexing for Hybrid Search on GPUs** *(accepted, to appear)*<br>Zhonggen Li, Yougen Li, Yifan Zhu, Congcong Ge, Guoteng Xu, Yunjun Gao [[arXiv]](https://arxiv.org/abs/2511.00855) `graph` `hybrid`<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>

**OSDI 2026**

- **Disentangling Graph Dependencies for Efficient Billion-Scale GPU Vector Search**<br>Haoru Zhao, Jingkai He, Jingyao Zeng, Mingkai Dong, Dong Du [[paper]](https://www.usenix.org/conference/osdi26/presentation/zhao) [[pdf]](https://www.usenix.org/system/files/osdi26-zhao.pdf) `graph`

**SIGMOD 2026**

- **CMANNS: GPU-Accelerated Graph Index Construction for ANNS via Compute-Memory Disaggregation**<br>Chengying Huan, Renjie Yao, Shaonan Ma, Rong Gu, Zhengyi Yang, Lizheng Chen, et al. [[paper]](https://doi.org/10.1145/3802027) `graph`
- **FlashANNS: GPU-Driven Asynchronous I/O Pipelining for Eliminating Storage-Compute Bottlenecks in Billion-Scale Similarity Search**<br>Yang Xiao, Mo Sun, Ziyu Song, Bing Tian, Jie Sun, Jie Zhang, et al. [[paper]](https://doi.org/10.1145/3786652) [[code]](https://github.com/Tinkerver/ann_search) `disk`
- **High-Throughput, Cost-Effective Billion-Scale Vector Search with a Single GPU**<br>Haodi Jiang, Hao Guo, Minhui Xie, Jiwu Shu, Youyou Lu [[paper]](https://doi.org/10.1145/3769799) [[code]](https://github.com/thustorage/GustANN) `billion-scale`
- **Scalable Graph Indexing using GPUs for Approximate Nearest Neighbor Search**<br>Zhonggen Li, Xiangyu Ke, Yifan Zhu, Bocheng Yu, Baihua Zheng, Yunjun Gao [[paper]](https://doi.org/10.1145/3769825) [[arXiv]](https://arxiv.org/abs/2508.08744) [[code]](https://github.com/ZJU-DAILY/Tagore) `graph`
- **VecFlow-Chamfer: A GPU-based Data Management System for High-Performance Multi-Vector Search on Superchips**<br>Chenghao Mo, Ben Karsin, Philip Adams, Minjia Zhang [[paper]](https://doi.org/10.1145/3786706) [[code]](https://github.com/Supercomputing-System-AI-Lab/VecFlow) `multi-vector`
- **VecFlow: A High-Performance Vector Data Management System for Filtered-Search on GPUs**<br>Jingyi Xi, Chenghao Mo, Ben Karsin, Artem M. Chirkin, Mingqin Li, Minjia Zhang [[paper]](https://doi.org/10.1145/3749189) [[arXiv]](https://arxiv.org/abs/2506.00812) [[code]](https://github.com/Supercomputing-System-AI-Lab/VecFlow)

**VLDB 2026**

- **GPU-Accelerated ANNS: Quantized for Speed, Built for Change**<br>Hunter McCoy, Zikun Wang, Prashant Pandey [[paper]](https://www.vldb.org/pvldb/vol19/p3413-pandey.pdf) [[code]](https://github.com/zikunw/jasper) `quantization` `dynamic`
- **GPU-Native Approximate Nearest Neighbor Search with IVF-RaBitQ: Fast Index Build and Search**<br>Jifan Shi, Jianyang Gao, James Xia, Tamas B. Fehér, Cheng Long [[paper]](https://www.vldb.org/pvldb/vol19/p3454-shi.pdf) [[code]](https://github.com/VectorDB-NTU/cuvs_rabitq) `quantization`
- **SVFusion: A CPU-GPU Co-Processing Architecture for Large-Scale Real-Time Vector Search**<br>Yuchen Peng, Dingyu Yang, Zhongle Xie, Ji Sun, Lidan Shou, Ke Chen, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1074-yang.pdf) [[code]](https://github.com/zjuDBxAI/svfusion) `dynamic`

**MLSys 2026**

- **TeleRAG: Efficient Retrieval-Augmented Generation Inference with Lookahead Retrieval**<br>Chien-Yu Lin, Keisuke Kamahori, Yiyu Liu, Xiaoxiang Shi, Madhav Kashyap, Yile Gu, et al. [[paper]](https://proceedings.mlsys.org/paper_files/paper/2026/hash/7fd522b89ac21009b7bbe7560a9a5add-Abstract-Conference.html) [[pdf]](https://proceedings.mlsys.org/paper_files/paper/2026/file/7fd522b89ac21009b7bbe7560a9a5add-Paper-Conference.pdf) [[code]](https://github.com/uw-syfi/TeleRAG) `rag`

**HPCA 2026**

- **VectorLiteRAG: Latency-Aware and Fine-Grained Resource Partitioning for Efficient RAG**<br>Junkyum Kim, Divya Mahajan [[paper]](https://doi.org/10.1109/HPCA68181.2026.11408552) [[arXiv]](https://arxiv.org/abs/2504.08930) [[code]](https://github.com/sitar-lab/VectorLiteRAG-AE) `rag` `ivf`

#### Out-of-Core ANNS Systems

_Indexes larger than DRAM, kept on SSD or disk, or spread across tiered or disaggregated memory._


**OSDI 2026**

- **The Clustering Strikes Back: Building Cost-Effective and High-Performance ANNS at Scale with Helmsman (Operational Systems)**<br>Yuchen Huang, Baiteng Ma, Yiping Sun, Yang Shi, Xiao Chen, Xiaocheng Zhong, et al. [[paper]](https://www.usenix.org/conference/osdi26/presentation/huang-yuchen) [[pdf]](https://www.usenix.org/system/files/osdi26-huang-yuchen.pdf) [[code]](https://github.com/Red-EAD/helmsman) `partition` `disk`

**SIGMOD 2026**

- **DiskJoin: Large-scale Vector Similarity Join with SSD**<br>Yanqi Chen, Xiao Yan, Alexandra Meliou, Eric Lo [[paper]](https://doi.org/10.1145/3769780) [[arXiv]](https://arxiv.org/abs/2508.18494) [[code]](https://github.com/iidyc/DiskJoin) `disk` `join`
- **Efficient Index Layout and Search Strategy for Large-scale High-dimensional Vector Similarity Search**<br>Weijian Chen, Haotian Liu, Yangshen Deng, Long Xiang, Liang Huang, Bo Tang [[paper]](https://doi.org/10.1145/3802045) [[code]](https://github.com/AlayaDB-AI/AlayaLite) `disk`
- **GPS: Revisiting the Data Layout for Disk-based High-Dimensional Vector Search**<br>Peiqi Yin, Xiao Yan, Qihui Zhou, Hui Li, Xiaolu Li, Meiling Wang, et al. [[paper]](https://doi.org/10.1145/3802069) [[code]](https://github.com/yinpeiqi/Gorgeous) `disk`

**OSDI 2025**

- **Achieving Low-Latency Graph-Based Vector Search via Aligning Best-First Search Algorithm with SSD**<br>Hao Guo, Youyou Lu [[paper]](https://www.usenix.org/conference/osdi25/presentation/guo) [[pdf]](https://www.usenix.org/system/files/osdi25-guo.pdf) [[code]](https://github.com/thustorage/PipeANN) `disk` `graph`

**VLDB 2025**

- **Select Edges Wisely: Monotonic Path Aware Graph Layout Optimization for Disk-based ANN Search**<br>Ziyang Yue, Bolong Zheng, Ling Xu, Kanru Xu, Shuhao Zhang, Yajuan Du, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p4337-zheng.pdf) [[code]](https://github.com/CodenameYZY/MARGO) `disk` `graph`
- **Turbocharging Vector Databases using Modern SSDs**<br>Joobo Shim, Jaewon Oh, Hongchan Roh, Jaeyoung Do, Sang-Won Lee [[paper]](https://www.vldb.org/pvldb/vol18/p4710-do.pdf) [[code]](https://github.com/FlashSQL/io-optimized-pgvector) `disk`

#### Distributed ANNS Systems

_Multi-node, RDMA, federated and scale-out vector search._


**SIGMOD 2027**

- **TITAN: A High-Throughput Distributed System for Approximate Nearest Neighbor Search on Large-scale Datasets** *(accepted, to appear)*<br>Ziyi Li, Angjun Lin, Yuhao Lin, Quanqing Xu, Ruixuan Zhang, Yuanyuan Zhu, et al.<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>

**SIGMOD 2026**

- **CoTra: Towards Efficient and Scalable Distributed Vector Search with RDMA**<br>Xiangyu Zhi, Meng Chen, Xiao Yan, Baotong Lu, Hui Li, Qianxi Zhang, et al. [[paper]](https://doi.org/10.1145/3786634) [[arXiv]](https://arxiv.org/abs/2507.06653) [[code]](https://github.com/xiangyuzhi/CoTra) `rdma`
- **HARMONY: A Scalable Distributed Vector Database for High-Throughput Approximate Nearest Neighbor Search**<br>Qian Xu, Feng Zhang, Chengxi Li, Lei Cao, Zheng Chen, Jidong Zhai, et al. [[paper]](https://doi.org/10.1145/3749167) [[arXiv]](https://arxiv.org/abs/2506.14707) [[code]](https://github.com/xuqianmamba/Harmony)

**VLDB 2026**

- **FedBridge: A Federated Query Engine over Embedding-Heterogeneous Vector Databases**<br>Yuxiang Wang, Ruixi Hu, Ziyuan He, Zhilin Liang, Xinyu Zhao, Yongxin Tong [[paper]](https://www.vldb.org/pvldb/vol19/p4498-tong.pdf) [[code]](https://github.com/Roy-buaa/FedBridge) `federated`
- **RED-ANNS: A RDMA-Enabled Distributed Framework for Graph-Based Approximate Nearest Neighbor Search**<br>Yue Chen, Kai Zhang, Sipeng Chen, Shihai Xiao, Xiaomin Zou, Ren Ren, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p399-chen.pdf) [[code]](https://github.com/cheenyuee/RED-ANNS) `rdma` `graph`

**VLDB 2025**

- **HAKES: Scalable Vector Database for Embedding Search Service**<br>Guoyu Hu, Shaofeng Cai, Tien Tuan Anh Dinh, Zhongle Xie, Cong Yue, Gang Chen, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p3049-ooi.pdf) [[code]](https://github.com/nusdbsystem/HAKES)
- **Unleashing Graph Partitioning for Large-Scale Nearest Neighbor Search**<br>Lars Gottesbüren, Laxman Dhulipala, Rajesh Jayaram, Jakub Lacki [[paper]](https://www.vldb.org/pvldb/vol18/p1649-gottesbueren.pdf) [[code]](https://github.com/larsgottesbueren/gp-ann) `partition`
- **VStream: A Distributed Streaming Vector Search System**<br>Shenghao Gong, Haobo Sun, Ziquan Fang, Liu Liu, Lu Chen, Yunjun Gao [[paper]](https://www.vldb.org/pvldb/vol18/p1593-gao.pdf) [[code]](https://github.com/ZJU-DAILY/VStream) `dynamic`

**ISCA 2025**

- **Hermes: Algorithm-System Co-design for Efficient Retrieval-Augmented Generation At-Scale**<br>Michael Shen, Muhammad Umar, Kiwan Maeng, et al. [[paper]](https://pure.psu.edu/en/publications/hermes-algorithm-system-co-design-for-efficient-retrieval-augment/) [[code]](https://github.com/S4AI-CornellTech/Hermes) `rag`

#### Vector Databases & Other Systems

_Vector databases and DBMS integration, CPU-efficient engines, privacy and security, and retrieval systems for RAG and KV caches._


**SIGMOD 2027**

- **Catching Inconsistencies in Vector Similarity Retrieval** *(accepted, to appear)*<br>Zixiao Huang, Ruochun Jin, Haotian Wang, Meng Zhang, Yuhua Tang `testing` `vector-db`<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>
- **Metric Algebra: Embedding-Independence in Vector Databases** *(accepted, to appear)*<br>Tianjian Yang, Yang Cao, Beining Yang, Ziying Chen, Tiejun Ma `embedding-models`<br><sub>SIGMOD 2027 round 1 (official accepted-papers page).</sub>
- **Phantom Neighbors: Information Leakage and Its Prevention in Access-Controlled Vector Databases** *(accepted, to appear)*<br>Yizheng Zhao `privacy` `access-control`<br><sub>SIGMOD 2027 round 2 (official accepted-papers page).</sub>

**VLDB 2027**

- **Can You Trust the Vectors in Your Vector Database? Black-Hole Attack from Embedding Space Defects** *(accepted, to appear)*<br>Hanxi Li, Jiale Lao, Zhengmao Ye, et al. [[arXiv]](https://arxiv.org/abs/2604.05480) [[code]](https://github.com/hanxi19/Black_Hole_Attack_for_Vector_Database) `security` `hubness`

**SIGMOD 2026**

- **HONEYBEE: Efficient Role-based Access Control for Vector Databases via Dynamic Partitioning**<br>Hongbin Zhong, Matthew Lentz, Nina Narodytska, Adriana Szekeres, Kexin Rong [[paper]](https://doi.org/10.1145/3786625) [[arXiv]](https://arxiv.org/abs/2505.01538) [[code]](https://github.com/rjzhb/VectorSearch-RBAC) `privacy` `access-control`
- **Integrating Vector Databases across Embedding Models**<br>Beining Yang, Yang Cao, Yang Ren [[paper]](https://doi.org/10.1145/3769803) `embedding-models`

**VLDB 2026**

- **Aker: Density-Aware Approximate Caching for Vector Search**<br>Sukjoon Oh, Minki Kang, Dohyun Kim, Baotong Lu, Jing Liu, Qianxi Zhang, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p2727-oh.pdf) [[code]](https://github.com/sjoon-oh/Aker) `caching`
- **Nova: A Multi-Purpose Vector Engine for Low-Latency, Multi-Tenant, and Cross-Table Hybrid Retrieval**<br>Dechuang Chen, Bing Chen, Jianwei Lu, Zhiwei Wu, Zeyu Yang, Qiang Gu, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p4453-zhou.pdf) `hybrid` `vector-db`
- **RetroInfer: A Vector Storage Engine for Scalable Long-Context LLM Inference**<br>Yaoqi Chen, Jinkai Zhang, Baotong Lu, Qianxi Zhang, Chengruidong Zhang, Jing Liu, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1016-lu.pdf) [[code]](https://github.com/microsoft/RetrievalAttention) `kvcache`
- **SQL-Native Vector Search at Billion Scale in Presto**<br>Zhichen Xu, Ge Gao, Ke Wang, Aakash Deep, Junjie Qi, Jort Gemmeke, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p4182-xu.pdf) `vector-db`
- **TEngineDB-V: An OLAP-Native Vector Search System for Large-𝑘 Workloads at Tencent**<br>Xufei Wu, Pengcheng Zhang, Yitong Song, Xiaobo Zhang, Anqi Liang, Kai Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p3955-zhou.pdf) `vector-db`
- **V3DB: Audit-on-Demand Zero-Knowledge Proofs for Verifiable Vector Search over Committed Snapshots**<br>Zipeng Qiu, Wenjie Qu, Jiaheng Zhang, Binhang Yuan [[paper]](https://www.vldb.org/pvldb/vol19/p2604-qiu.pdf) [[code]](https://github.com/TabibitoQZP/zk-IVF-PQ) `zkp` `verifiable`

**MLSys 2026**

- **LEANN: A Low-Storage Overhead Vector Index**<br>Yichuan Wang, Zhifei Li, Shu Liu, Yongji Wu, Ziming Mao, Yilong Zhao, et al. [[paper]](https://proceedings.mlsys.org/paper_files/paper/2026/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) [[pdf]](https://proceedings.mlsys.org/paper_files/paper/2026/file/e27ea0cd50b798ff8942caf9203f0992-Paper-Conference.pdf) [[code]](https://github.com/yichuan-w/LEANN) `storage` `graph`

**OSDI 2025**

- **Compass: Encrypted Semantic Search with High Accuracy**<br>Jinhao Zhu, Liana Patel, Matei Zaharia, Raluca Ada Popa [[paper]](https://www.usenix.org/conference/osdi25/presentation/zhu-jinhao) [[pdf]](https://www.usenix.org/system/files/osdi25-zhu-jinhao.pdf) [[code]](https://github.com/Clive2312/compass) `privacy`
- **Quake: Adaptive Indexing for Vector Search**<br>Jason Mohoney, Devesh Sarda, Mengze Tang, Shihabur Rahman Chowdhury, Anil Pacaci, Ihab F. Ilyas, et al. [[paper]](https://www.usenix.org/conference/osdi25/presentation/mohoney) [[pdf]](https://www.usenix.org/system/files/osdi25-mohoney.pdf) [[code]](https://github.com/marius-team/quake) `dynamic` `partition`

**SIGMOD 2025**

- **Accelerating Graph Indexing for ANNS on Modern CPUs**<br>Mengzhao Wang, Haotian Wu, Xiangyu Ke, Yunjun Gao, Yifan Zhu, Wenchao Zhou [[paper]](https://doi.org/10.1145/3725260) [[arXiv]](https://arxiv.org/abs/2502.18113) [[code]](https://github.com/ZJU-DAILY/HNSW-Flash) `graph` `cpu`
- **PDX: A Data Layout for Vector Similarity Search**<br>Leonardo Kuffó, Elena Krippner, Peter Boncz [[paper]](https://doi.org/10.1145/3725333) [[arXiv]](https://arxiv.org/abs/2503.04422) [[code]](https://github.com/cwida/PDX) `layout`
- **PQCache: Product Quantization-based KVCache for Long Context LLM Inference**<br>Hailin Zhang, Xiaodong Ji, Yilin Chen, Fangcheng Fu, Xupeng Miao, Xiaonan Nie, et al. [[paper]](https://doi.org/10.1145/3725338) [[arXiv]](https://arxiv.org/abs/2407.12820) [[code]](https://github.com/HugoZHL/PQCache) `kvcache` `quantization`
- **Tribase: A Vector Data Query Engine for Reliable and Lossless Pruning Compression using Triangle Inequalities**<br>Qian Xu, Juan Yang, Feng Zhang, Junda Pan, Kang Chen, Youren Shen, et al. [[paper]](https://doi.org/10.1145/3709743) [[code]](https://github.com/xuqianmamba/Tribase)

**VLDB 2025**

- **Cost-Effective, Low Latency Vector Search with Azure Cosmos DB**<br>Nitish Upreti, Harsha Vardhan Simhadri, Hari Sudan Sundar, Krishnan Sundaram, Samer Boshra, Balachandar Perumalswamy, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p5166-upreti.pdf) `vector-db` `cloud`
- **FedVSE: A Privacy-Preserving and Efficient Vector Search Engine for Federated Databases**<br>Zeheng Fan, Yuxiang Zeng, Zhuanglin Zheng, Yongxin Tong [[paper]](https://www.vldb.org/pvldb/vol18/p5371-tong.pdf) `privacy` `federated`
- **GaussDB-Vector: A Large-Scale Persistent Real-Time Vector Database for LLM Applications**<br>Guoliang Li, Ji Sun, James Pan, Jiang Wang, Yongqing Xie, Ruicheng Liu, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p4951-sun.pdf) `vector-db`
- **NaviX: A Native Vector Index Design for Graph DBMSs With Robust Predicate-Agnostic Search Performance**<br>Gaurav Sehgal, Semih Salihoglu [[paper]](https://www.vldb.org/pvldb/vol18/p4438-sehgal.pdf) [[code]](https://github.com/gaurav8297/kuzu) `filtered` `graph-dbms`
- **VSAG: An Optimized Search Framework for Graph-based Approximate Nearest Neighbor Search**<br>Xiaoyao Zhong, Haotian Li, Jiabao Jin, Mingyu Yang, Deming Chu, Xiangyu Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p5017-cheng.pdf) [[code]](https://github.com/antgroup/vsag) `graph`

**ISCA 2025**

- **RAGO: Systematic Performance Optimization for Retrieval-Augmented Generation Serving**<br>Wenqi Jiang, Suvinay Subramanian, Cat Graves, et al. [[paper]](https://doi.org/10.1145/3695053.3731093) [[arXiv]](https://arxiv.org/abs/2503.14649) [[code]](https://github.com/google/rago) `rag`

### Architecture

#### FPGA & In-storage Acceleration

_Vector search on FPGAs and inside storage devices (computational SSDs, in-flash/NAND processing)._


**MICRO 2026**

- **D-NOVA: In-Storage Retrieval Accelerator via Dual-Bound 3D NAND-Optimized Similarity Search with Vector Adaptation** *(accepted, to appear)*<br>Chang Eun Song, Sumukh Pinge, Tianqi Zhang, et al. [[arXiv]](https://arxiv.org/abs/2607.17538) `in-storage` `in-flash` `ivf` `rag`<br><sub>Listed in the MICRO 2026 program (Session 9B).</sub>
- **NiF: Hybrid In-Flash and In-Storage Acceleration for Approximate Nearest Neighbor Search** *(accepted, to appear)*<br>Myoungjun Chun, et al. `in-storage` `in-flash`<br><sub>Listed in the MICRO 2026 program (Session 4A).</sub>
- **WiFlash: Wordline-Parallel Approximate Nearest Neighbor Search Inside Flash Cell Array** *(accepted, to appear)*<br>Hyunjin Kim, Juchan Lee, Inseong Choi, et al. `in-flash`<br><sub>Listed in the MICRO 2026 program (Session 9B).</sub>

**VLDB 2025**

- **Chameleon: a Heterogeneous and Disaggregated Accelerator System for Retrieval-Augmented Language Models**<br>Wenqi Jiang, Marco Zeller, Roger Waleffe, Torsten Hoefler, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p42-jiang.pdf) [[code]](https://github.com/WenqiJiang/Chameleon) `rag` `disaggregated`
- **Fast Graph Vector Search via Hardware Acceleration and Delayed-Synchronization Traversal**<br>Wenqi Jiang, Hang Hu, Torsten Hoefler, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p3797-jiang.pdf) [[code]](https://github.com/fpgasystems/Falcon-accelerate-graph-vector-search) `fpga` `graph`

**ISCA 2025**

- **In-Storage Acceleration of Retrieval Augmented Generation as a Service**<br>Rohan Mahapatra, Harsha Santhanam, Christopher Priebe, et al. [[paper]](https://doi.org/10.1145/3695053.3731032) `in-storage` `rag`
- **REIS: A High-Performance and Energy-Efficient Retrieval System with In-Storage Processing**<br>Kangqi Chen, Andreas Kosmas Kakolyris, Rakesh Nadig, Manos Frouzakis, et al. [[arXiv]](https://arxiv.org/abs/2506.16444) `in-storage` `ivf` `rag`

#### Domain-specific Accelerators

_ASICs and processing-in/near-memory (PIM/NDP) designs. GPU software belongs under Systems._


**ISCA 2026**

- **NasZip: Software and Hardware Co-design to Accelerate Approximate Nearest Neighbor Search with DIMM-based Near-Data Processing**<br>Cheng Zou, S. Yang, C. Nie, et al. [[paper]](https://doi.org/10.1109/ISCA66397.2026.00105) [[arXiv]](https://arxiv.org/abs/2605.21952) [[code]](https://github.com/Intelligent-Computing-Research-Group/NasZip) `near-memory` `early-termination` `graph`

**MICRO 2026**

- **MFNNS: A Multiplier-Free Near-Memory Accelerator for Graph-based ANNS** *(accepted, to appear)*<br>Rui Meng, Yonghao Chen, Jiaxiang Zou, et al. `near-memory` `graph`<br><sub>Listed in the MICRO 2026 program (Session 9B).</sub>

**SC 2026**

- **PIMCQG: Co-Designing Billion-Scale Graph-Based Approximate Nearest Neighbor Search for Processing-in-Memory** *(accepted, to appear)*<br>Sitian Chen, Yusen Li, Yao Chen, et al. [[arXiv]](https://arxiv.org/abs/2605.25522) [[code]](https://github.com/steam009/PIMCQG) `pim` `graph` `quantization` `billion-scale`<br><sub>Acceptance per the code README and <a href="https://amelieczhou.github.io/publications.html">author homepage</a>.</sub>

**ASPLOS 2025**

- **Accelerating Retrieval-Augmented Generation**<br>Derrick Quinn, Mohammad Nouri, Neel Patel, John Salihu, Alireza Salemi, Sukhan Lee, et al. [[paper]](https://doi.org/10.1145/3669940.3707264) [[arXiv]](https://arxiv.org/abs/2412.15246) [[code]](https://github.com/architecture-research-group/iks_simulator) `rag` `near-memory`

**ISCA 2025**

- **ANSMET: Approximate Nearest Neighbor Search with Near-Memory Processing and Hybrid Early Termination**<br>Yiwei Li, Yuxin Jin, Boyu Tian, et al. [[paper]](https://doi.org/10.1145/3695053.3731013) [[pdf]](https://people.iiis.tsinghua.edu.cn/~gaomy/pubs/ansmet.isca25.pdf) [[code]](https://github.com/tsinghua-ideal/ANSMET) `near-memory` `early-termination`
- **DReX: Accurate and Scalable Dense Retrieval Acceleration via Algorithmic-Hardware Codesign**<br>Derrick Quinn, E. Ezgi Yücel, Martin Prammer, et al. [[paper]](https://par.nsf.gov/biblio/10634219) `near-memory` `rag`
- **HeterRAG: Heterogeneous Processing-in-Memory Acceleration for Retrieval-augmented Generation**<br>Chaoqiang Liu, Haifeng Liu, Dan Chen, et al. `pim` `rag`

**MICRO 2025**

- **Accelerating Retrieval Augmented Language Model via PIM and PNM Integration**<br>Je-Woo Jang, Junyong Oh, et al. [[paper]](https://doi.org/10.1145/3725843.3756020) `pim` `near-memory` `ivf` `quantization` `rag`

**HPCA 2025**

- **AccelES: Accelerating Top-K SpMV for Embedding Similarity via Low-bit Pruning**<br>Jiaqi Zhai, Xuanhua Shi, Kaiyi Huang, et al. [[paper]](https://doi.org/10.1109/HPCA61900.2025.00077) `exact-search` `sparse`<br><sub>Exact (not approximate) top-K embedding similarity search; adjacent to ANNS.</sub>
- **NeuVSA: A Unified and Efficient Accelerator for Neural Vector Search**<br>Ziming Yuan, Lei Dai, Wen Li, et al. [[paper]](https://doi.org/10.1109/HPCA61900.2025.00065) `quantization` `learned`

**SC 2025**

- **DRIM-ANN: An Approximate Nearest Neighbor Search Engine based on Commercial DRAM-PIMs**<br>Mingkai Chen, Tianhua Han, Cheng Liu, et al. [[paper]](https://doi.org/10.1145/3712285.3759801) [[arXiv]](https://arxiv.org/abs/2410.15621) [[code]](https://github.com/KMC20/DRIM-ANN) `pim` `ivf` `quantization`
- **UpANNS: Enhancing Billion-Scale ANNS Efficiency with Real-World PIM Architecture**<br>Sitian Chen, Amelie Chi Zhou, Yucheng Shi, et al. [[paper]](https://doi.org/10.1145/3712285.3759777) [[arXiv]](https://arxiv.org/abs/2410.23805) [[code]](https://github.com/steam009/UpANNS) `pim` `ivf` `quantization` `billion-scale`

### Experiments & Analysis

#### Benchmarks

_Benchmark suites and frameworks, and experimental evaluations that compare existing methods._


**VLDB 2027**

- **DiskVecLab: A Deployment-Realistic Evaluation Framework for Disk-Based Vector Search** *(accepted, to appear)*<br>Yuxiang Wang, Yongxin Tong, Shuyuan Li, et al. [[code]](https://github.com/alibaba/DiskVecLab) `disk`

**SIGMOD 2026**

- **Attribute Filtering in Approximate Nearest Neighbor Search: An In-depth Experimental Study**<br>Mocheng Li, Xiao Yan, Baotong Lu, Yue Zhang, James Cheng, Chenhao Ma [[paper]](https://doi.org/10.1145/3769763) [[arXiv]](https://arxiv.org/abs/2508.16263) [[code]](https://github.com/lmccccc/FANNBench) `filtered`
- **CANDOR-Bench: Benchmarking In-Memory Continuous ANNS under Dynamic Open-World Streams [Experiments & Analysis]**<br>Mingqi Wang, Junyao Dong, Zhuoyan Wu, Jun Liu, Ruicheng Zhang, Jianjun Zhao, et al. [[paper]](https://doi.org/10.1145/3786630) [[code]](https://github.com/DataSysResearch/CANDOR-Bench) `dynamic`
- **Reveal Hidden Pitfalls and Navigate Next Generation of Vector Similarity Search from Task-Centric Views: [Experiments & Analysis]**<br>Tingyang Chen, Cong Fu, Jiahua Wu, Haotian Wu, Hua Fan, Xiangyu Ke, et al. [[paper]](https://doi.org/10.1145/3786690) [[arXiv]](https://arxiv.org/abs/2512.12980) [[code]](https://github.com/ZJU-DAILY/Iceberg)
- **VecBench: A Controllable Benchmark for Filtered Vector Search: [Experiments & Analysis]**<br>Xiang Zhang, Chao Zhang, Ju Fan, Guoliang Li, Xiaoyong Du [[paper]](https://doi.org/10.1145/3802125) [[code]](https://github.com/ruc-datalab/VecBench) `filtered`

**VLDB 2026**

- **An Experimental Evaluation of Hybrid Querying on Vectors**<br>Jiaxu Zhu, Jiayu Yuan, Kaiwen Yang, Xiaobao Chen, Shihuan Yu, Hongchang Lv, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p183-zheng.pdf) [[code]](https://github.com/zhujx001/Hybrid-ANNS-Experiment) `filtered`
- **Balancing the Blend: An Experimental Analysis of Trade-offs in Hybrid Search**<br>Mengzhao Wang, Boyu Tan, Yunjun Gao, Hai Jin, Yingfeng Zhang, Xiangyu Ke, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1715-gao.pdf) [[code]](https://github.com/infiniflow/infinity) `hybrid`
- **Disk-Resident Graph ANN Search: An Experimental Evaluation** *(accepted, to appear)*<br>Xiaoyu Chen, Jinxiu Qu, Yitong Song, et al. [[arXiv]](https://arxiv.org/abs/2603.01779) [[code]](https://github.com/hkbudb/disk-vss-survey) `disk` `graph`<br><sub>PVLDB 2026 per the code README; not yet in DBLP.</sub>
- **Revisiting Filtered ANN Benchmarks: A Hardness-Controlled Benchmark Generator for Realistic Evaluation**<br>Mintaek Lim, Dogeun Kim, Minwoo Kim, Jaeyoung Do [[paper]](https://www.vldb.org/pvldb/vol19/p2763-lim.pdf) [[code]](https://github.com/AIDAS-Lab/FANN_Benchmark) `filtered`
- **Towards Robustness: A Critique of Current Vector Database Assessments** *(accepted, to appear)*<br>Zikai Wang, Qianxi Zhang, Baotong Lu, et al. [[arXiv]](https://arxiv.org/abs/2507.00379) [[code]](https://github.com/khaiwang/ANN-Robustness-Submission) `robustness`<br><sub>VLDB 2026 per the artifact README; not yet in DBLP.</sub>

**SIGMOD 2025**

- **Graph-Based Vector Search: An Experimental Evaluation of the State-of-the-Art**<br>Ilias Azizi, Karima Echihabi, Themis Palpanas [[paper]](https://doi.org/10.1145/3709693) [[arXiv]](https://arxiv.org/abs/2502.05575) [[code]](https://github.com/iliasazizi/GVS) `graph`

**VLDB 2025**

- **BigVectorBench: Heterogeneous Data Embedding and Compound Queries are Essential in Evaluating Vector Databases**<br>Guoxin Kang, Zhongxin Ge, Jingpei Hu, Xueya Zhang, Lei Wang, Jianfeng Zhan [[paper]](https://www.vldb.org/pvldb/vol18/p1536-zhan.pdf) [[code]](https://github.com/BenchCouncil/BigVectorBench)

#### Workload Characterization

_In-depth analyses of where time, I/O and memory go; design-space explorations; characterization on specific hardware or systems._


**SIGMOD 2026**

- **An In-Depth Study of Filter-Agnostic Vector Search on a PostgreSQL Database System: [Experiments & Analysis]**<br>Duo Lu, Helena Caminal, Manos Chatzakis, Yannis Papakonstantinou, Yannis Chronis, Vaibhav Jain, et al. [[paper]](https://doi.org/10.1145/3802011) [[arXiv]](https://arxiv.org/abs/2603.23710) [[code]](https://github.com/google-systems-research/fvs) `filtered` `postgres`
- **Building Stateless Serverless Vector DBs via Block-based Data Partitioning**<br>Daniel Barcelona Pons, Raúl Gracia Tinedo, Albert Cañadilla-Domingo, Xavier Roca-Canals, Pedro García López [[paper]](https://doi.org/10.1145/3769769) [[code]](https://github.com/neardata-eu/serverless-vdb) `serverless`
- **Through the Lens of Hubness: A Revisit on Graph-Based Approximate Nearest Neighbor Search: [Experiments & Analysis]**<br>Xiaoliang Xu, Haonan Dai, Can Li, Mengzhao Wang, Qiang Yue [[paper]](https://doi.org/10.1145/3802120) [[code]](https://github.com/H40NaN/GraphANNS-Hubness) `graph`

**VLDB 2026**

- **I/O Optimizations in Graph-Based Disk-Resident Approximate Nearest Neighbor Search: A Design Space Exploration**<br>Liang Li, Shufeng Gong, Yanan Yang, Yiduo Wang, Jie Wu [[paper]](https://www.vldb.org/pvldb/vol19/p1484-li.pdf) [[code]](https://github.com/LeonLee666/IObench4DiskANN) `disk`

**MICRO 2025**

- **Characterizing and Optimizing Realistic Workloads on a Commercial Compute-in-SRAM Device**<br>Niansong Zhang, Wenbo Zhu, Courtney Golden, et al. [[paper]](https://doi.org/10.1145/3725843.3756132) [[arXiv]](https://arxiv.org/abs/2509.05451) [[code]](https://github.com/cornell-zhang/apu-micro25-artifact) `compute-in-sram` `rag`<br><sub>Characterization paper; its main case study is RAG retrieval on the GSI APU.</sub>

#### Surveys

_Surveys and tutorials._


**VLDB 2026**

- **Advances of Query Processing in Vector Databases**<br>Jiadong Xie, Yingfan Liu, Jeffrey Xu Yu [[paper]](https://www.vldb.org/pvldb/vol19/p4893-xie.pdf)

**VLDB 2025**

- **Filtered Vector Search: State-of-the-art and Research Challenges**<br>Helena Caminal, Yannis Chronis, Yannis Papakonstantinou, Fatma Özcan, Anastasia Ailamaki [[paper]](https://www.vldb.org/pvldb/vol18/p5488-caminal.pdf) `filtered`
<!-- END GENERATED -->
