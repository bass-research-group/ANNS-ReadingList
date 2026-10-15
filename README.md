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

- **Scope**: approximate nearest neighbor search (ANNS) and vector search — algorithms, systems, and accelerators — published at
  SOSP, OSDI, ASPLOS, SIGMOD, VLDB, MLSys, ISCA, MICRO, HPCA, SC, and PPoPP, **from 2025 on**.
  RAG / KV-cache papers are included only when vector retrieval is the core of the paper.
- **Sub-topics**: every paper is tagged with exactly one of
  - *Algorithms*: index structures (graph, IVF, trees), quantization, filtered/hybrid search, early termination, theory, algorithmic benchmarks;
  - *Systems*: vector databases, disk/SSD-resident and distributed search, updates, DBMS integration, privacy, retrieval for RAG / KV cache;
  - *Accelerators*: GPU, FPGA, ASIC, processing-in/near-memory, in-storage, and CXL-based vector search.
- **Views**: the sections below list papers by sub-topic; [`papers/by-venue/`](papers/by-venue/) lists them per conference.
- **Sources**: [DBLP](https://dblp.org/) (via the DBLP-derived lists of [csconf-papers](https://github.com/RealZST/csconf-papers)),
  official conference programs, and authors' preprints that state acceptance. Papers known only from such evidence are marked *(accepted, to appear)*.

## Contributing / updating

All content lives in [`data/papers.yaml`](data/papers.yaml). After editing it, run

```sh
python3 scripts/build.py            # regenerates README.md (between the markers) and papers/by-venue/*.md
python3 scripts/find_candidates.py  # lists new DBLP hits not yet in papers.yaml or data/excluded.txt
```

## Paper list

<!-- BEGIN GENERATED -->
There are **146** papers so far.

| Venue | 2025 | 2026 | Total |
|---|---|---|---|
| [SOSP](papers/by-venue/SOSP.md) | — | — | 0 |
| [OSDI](papers/by-venue/OSDI.md) | 3 | 2 | 5 |
| [ASPLOS](papers/by-venue/ASPLOS.md) | 1 | — | 1 |
| [SIGMOD](papers/by-venue/SIGMOD.md) | 16 | 43 | 59 |
| [VLDB](papers/by-venue/VLDB.md) | 26 | 31 | 57 |
| [MLSys](papers/by-venue/MLSys.md) | — | 3 | 3 |
| [ISCA](papers/by-venue/ISCA.md) | 7 | 1 | 8 |
| [MICRO](papers/by-venue/MICRO.md) | 2 | 4 | 6 |
| [HPCA](papers/by-venue/HPCA.md) | 2 | 1 | 3 |
| [SC](papers/by-venue/SC.md) | 2 | 1 | 3 |
| [PPoPP](papers/by-venue/PPoPP.md) | 1 | — | 1 |

| Sub-topic | 2025 | 2026 | Total |
|---|---|---|---|
| [Algorithms](#algorithms) | 26 | 47 | 73 |
| [Systems](#systems) | 20 | 23 | 43 |
| [Accelerators](#accelerators) | 14 | 16 | 30 |

## Papers by sub-topic

### Algorithms

_Index structures (graph, IVF, trees), quantization, filtered/hybrid search, early termination, theory, and algorithmic benchmarks._

#### SIGMOD 2026

- **Accelerating High-Dimensional ANN Search via Skipping Redundant Distance Computations**<br>Ziwen Song, Bin Wang, Xiaochun Yang [[paper]](https://doi.org/10.1145/3769753)
- **Attribute Filtering in Approximate Nearest Neighbor Search: An In-depth Experimental Study**<br>Mocheng Li, Xiao Yan, Baotong Lu, Yue Zhang, James Cheng, Chenhao Ma [[paper]](https://doi.org/10.1145/3769763) [[arXiv]](https://arxiv.org/abs/2508.16263) `filtered` `benchmark`
- **Beyond Vector Search: Querying With and Without Predicates**<br>Jiadong Xie, Jeffrey Xu Yu, Siyi Teng, Yingfan Liu [[paper]](https://doi.org/10.1145/3769765) `filtered`
- **CANDOR-Bench: Benchmarking In-Memory Continuous ANNS under Dynamic Open-World Streams [Experiments & Analysis]**<br>Mingqi Wang, Junyao Dong, Zhuoyan Wu, Jun Liu, Ruicheng Zhang, Jianjun Zhao, et al. [[paper]](https://doi.org/10.1145/3786630) `dynamic` `benchmark`
- **Curator: Efficient Vector Search with Low-Selectivity Filters**<br>Yicheng Jin, Yongji Wu, Wenjun Hu, Bruce M. Maggs, Jun Yang, Xiao Zhang, et al. [[paper]](https://doi.org/10.1145/3786635) [[arXiv]](https://arxiv.org/abs/2601.01291) `filtered`
- **DARTH: Declarative Recall Through Early Termination for Approximate Nearest Neighbor Search**<br>Manos Chatzakis, Yannis Papakonstantinou, Themis Palpanas [[paper]](https://doi.org/10.1145/3749160) [[arXiv]](https://arxiv.org/abs/2505.19001) `early-termination`
- **Distribution-Aware Exploration for Adaptive HNSW Search**<br>Chao Zhang, Renée J. Miller [[paper]](https://doi.org/10.1145/3786639) [[arXiv]](https://arxiv.org/abs/2512.06636) `graph`
- **Dynamically Detect and Fix Hardness for Efficient Approximate Nearest Neighbor Search**<br>Zhiyuan Hua, Qiji Mo, Zebin Yao, Lixiao Cui, Xiaoguang Liu, Gang Wang, et al. [[paper]](https://doi.org/10.1145/3769783) `graph`
- **Efficient and Robust Out-Of-Distribution Vector Similarity Search with Cross-Distribution Monotonic Graph**<br>Qiang Yue, Mengzhao Wang, Xiaoliang Xu, Cheng Long, Yuxiang Wang, Jiahui Wang [[paper]](https://doi.org/10.1145/3786643) `graph` `ood`
- **Efficient Approximate Nearest Neighbor Search via Hemi-Sphere Centroids Graph**<br>Runwen Qiu, Jing Tang [[paper]](https://doi.org/10.1145/3769786) `graph`
- **Efficient Vector Index Merging in Vector Databases**<br>Chenzhe Jin, Yunan Zhang, Jiayi Liu, Jianguo Wang [[paper]](https://doi.org/10.1145/3786645) `merging`
- **Enhancing Graph-based Approximate Maximum Inner Product Search via Norm-Adaptive Partitioning**<br>Xi Zhao, Zhoujin Tian, Kai Huang, Yao Tian, Xiaokui Xiao, Bolong Zheng, et al. [[paper]](https://doi.org/10.1145/3802051) `mips` `graph`
- **Fast-Convergent Proximity Graphs for Approximate Nearest Neighbor Search**<br>Binhong Li, Xiao Yan, Shangqi Lu [[paper]](https://doi.org/10.1145/3786650) [[arXiv]](https://arxiv.org/abs/2510.05975) `graph`
- **FAVOR: Efficient Filter-Agnostic Vector ANNS Based on Selectivity-Aware Exclusion Distances**<br>Junjie Song, Yu Liu, Guoyu Hu, Zhongle Xie, Ming Yang, Beng Chin Ooi, et al. [[paper]](https://doi.org/10.1145/3802060) [[arXiv]](https://arxiv.org/abs/2605.07770) `filtered`
- **FGIM: a Fast Graph-based Indexes Merging Framework for Approximate Nearest Neighbor Search**<br>Zekai Wu, Jiabao Jin, Peng Cheng, Xiaoyao Zhong, Lei Chen, Yongxin Tong, et al. [[paper]](https://doi.org/10.1145/3786651) [[arXiv]](https://arxiv.org/abs/2603.21710) `graph` `merging`
- **GEM: A Native Graph-based Index for Multi-Vector Retrieval**<br>Yao Tian, Zhoujin Tian, Xi Zhao, Ruiyuan Zhang, Xiaofang Zhou [[paper]](https://doi.org/10.1145/3802065) [[arXiv]](https://arxiv.org/abs/2603.20336) `multi-vector` `graph`
- **LM-Tree: A Hybrid Learned Index for Similarity Search in Metric Spaces**<br>Yaqi Wang, Bin Wang, Rui Zhu, Wenli Sun, Xiaochun Yang [[paper]](https://doi.org/10.1145/3786665) `metric-space` `learned`
- **On Efficient Approximate Aggregate Nearest Neighbor Queries over Learned Representations**<br>Carrie Wang, Sihem Amer-Yahia, Laks V. S. Lakshmanan, Reynold Cheng [[paper]](https://doi.org/10.1145/3786672) [[arXiv]](https://arxiv.org/abs/2502.18803)
- **PathSeer: Adaptive Neighbor Handling for Efficient Filtered ANN Search**<br>Zhiyue Li, Guangyan Zhang, Ruochun Jin, Bojun Li, Xiaoguang Ren, Wenjing Yang [[paper]](https://doi.org/10.1145/3802098) `filtered`
- **PGTuner: An Efficient Framework for Automatic and Transferable Configuration Tuning of Proximity Graphs**<br>Hao Duan, Yitong Song, Bin Yao, Anqi Liang [[paper]](https://doi.org/10.1145/3749179) [[arXiv]](https://arxiv.org/abs/2508.17886) `graph` `tuning`
- **RAIRS: Optimizing Redundant Assignment and List Layout for IVF-Based ANN Search**<br>Zehai Yang, Shimin Chen [[paper]](https://doi.org/10.1145/3786687) [[arXiv]](https://arxiv.org/abs/2601.07183) `ivf`
- **Reveal Hidden Pitfalls and Navigate Next Generation of Vector Similarity Search from Task-Centric Views: [Experiments & Analysis]**<br>Tingyang Chen, Cong Fu, Jiahua Wu, Haotian Wu, Hua Fan, Xiangyu Ke, et al. [[paper]](https://doi.org/10.1145/3786690) [[arXiv]](https://arxiv.org/abs/2512.12980) `benchmark`
- **SAQ: Pushing the Limits of Vector Quantization through Code Adjustment and Dimension Segmentation**<br>Hui Li, Shiyuan Deng, Xiao Yan, Xiangyu Zhi, James Cheng [[paper]](https://doi.org/10.1145/3769824) [[arXiv]](https://arxiv.org/abs/2509.12086) `quantization`
- **TaCo: Data-adaptive and Query-aware Subspace Collision for High-dimensional Approximate Nearest Neighbor Search**<br>Jiuqi Wei, Zhenyu Liao, Ruoyu Han, Quanqing Xu, Chuanhui Yang, Themis Palpanas [[paper]](https://doi.org/10.1145/3802118) [[arXiv]](https://arxiv.org/abs/2603.24919)
- **Through the Lens of Hubness: A Revisit on Graph-Based Approximate Nearest Neighbor Search: [Experiments & Analysis]**<br>Xiaoliang Xu, Haonan Dai, Can Li, Mengzhao Wang, Qiang Yue [[paper]](https://doi.org/10.1145/3802120) `graph` `benchmark`
- **TRIM: Accelerating High-Dimensional Vector Similarity Search with Enhanced Triangle-Inequality-Based Pruning**<br>Yitong Song, Pengcheng Zhang, Chao Gao, Bin Yao, Kai Wang, Zongyuan Wu, et al. [[paper]](https://doi.org/10.1145/3769838)
- **VecBench: A Controllable Benchmark for Filtered Vector Search: [Experiments & Analysis]**<br>Xiang Zhang, Chao Zhang, Ju Fan, Guoliang Li, Xiaoyong Du [[paper]](https://doi.org/10.1145/3802125) `filtered` `benchmark`
- **WoW: A Window-to-Window Incremental Index for Range-Filtering Approximate Nearest Neighbor Search**<br>Ziqi Wang, Jingzhe Zhang, Wei Hu [[paper]](https://doi.org/10.1145/3769843) [[arXiv]](https://arxiv.org/abs/2508.18617) `filtered`

#### VLDB 2026

- **A Topology-Aware Localized Update Strategy for Graph-Based ANN Index**<br>Song Yu, Shengyuan Lin, Shufeng Gong, Yongqing Xie, Ruicheng Liu, Yijie Zhou, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p495-yu.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p495-yu.pdf) `graph` `dynamic`
- **Advances of Query Processing in Vector Databases**<br>Jiadong Xie, Yingfan Liu, Jeffrey Xu Yu [[paper]](https://www.vldb.org/pvldb/vol19/p4893-xie.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p4893-xie.pdf) `survey`
- **An Experimental Evaluation of Hybrid Querying on Vectors**<br>Jiaxu Zhu, Jiayu Yuan, Kaiwen Yang, Xiaobao Chen, Shihuan Yu, Hongchang Lv, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p183-zheng.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p183-zheng.pdf) `filtered` `benchmark`
- **ANNiE: A Learned Query Cost Estimator for Graph-Based Approximate Nearest Neighbor Search**<br>Zeyu Wang, Manos Chatzakis, Qitong Wang, Themis Palpanas, Peng Wang, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p3820-wang.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3820-wang.pdf) `graph` `cost-model`
- **BBC: Improving Large-𝑘 Approximate Nearest Neighbor Search with a Bucket-based Result Collector**<br>Ziqi Yin, Gao Cong, Kai Zeng, Jinwei Zhu, Bin Cui [[paper]](https://www.vldb.org/pvldb/vol19/p3468-yin.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3468-yin.pdf) `large-k`
- **CGIF: Combining Proximity Graphs and Inverted Files for Efficient Filtered Vector Search over Arbitrary Predicates**<br>Jiarui Luo, Chaoji Zuo, Dong Deng [[paper]](https://www.vldb.org/pvldb/vol19/p3663-luo.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3663-luo.pdf) `filtered`
- **ConANN: Conformal Approximate Nearest Neighbor Search**<br>Sonia Horchidan, Fabian Zeiher, Henrik Boström, Paris Carbone [[paper]](https://www.vldb.org/pvldb/vol19/p29-horchidan.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p29-horchidan.pdf)
- **CONDA: A Connectivity-Aware Dynamic Index for Approximate Nearest Neighbor Search over Evolving Data**<br>Darae Lee, Min-Soo Kim [[paper]](https://www.vldb.org/pvldb/vol19/p3357-lee.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3357-lee.pdf) `dynamic` `graph`
- **Elastic Index Selection for Label-Hybrid AKNN Search**<br>Mingyu Yang, Wenxuan Xia, Wentao Li, Raymond Chi-Wing Wong, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p617-yang.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p617-yang.pdf) `filtered`
- **GAS: A Lightweight Framework for Filtered Search over Wide-table Vectors**<br>Ziyuan He, Yuxiang Wang, Yu Sun, Zijie Ma, Hui Li, Qian Tao, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p3133-tong.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3133-tong.pdf) `filtered`
- **Harmonizing Efficiency and Accuracy in Filtered Vector Search**<br>Zixiang Zhou, Xuhao Chen [[paper]](https://www.vldb.org/pvldb/vol19/p2059-chen.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p2059-chen.pdf) `filtered`
- **HEXA: A Disjoint-Subgraph-Based Indexing Framework for Approximate Nearest Neighbor Search at Billion Scale**<br>Yifei Xu, Yanyan Shen, Youmin Chen, Linpeng Huang [[paper]](https://www.vldb.org/pvldb/vol19/p2922-shen.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p2922-shen.pdf) `graph` `billion-scale`
- **JHQ: Johnson-Lindenstrauss Enhanced Hierarchical Quantization for High-Dimensional Approximate Nearest Neighbor Search**<br>Jiabao Han, Mengxuan Zhang, Goce Trajcevski [[paper]](https://www.vldb.org/pvldb/vol19/p1530-han.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p1530-han.pdf) `quantization`
- **QBAT: Model-based Query Budget Autotuner for Clustering-based Approximate Nearest Neighbor Search**<br>Jonghyun Bae, Tae Jun Ham, Alan Li, Supawit Chockchowwat, Yannis Papakonstantinou [[paper]](https://www.vldb.org/pvldb/vol19/p3091-chockchowwat.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3091-chockchowwat.pdf) `ivf` `tuning`
- **Quantization Meets Projection: A Happy Marriage for Approximate k-Nearest Neighbor Search**<br>Mingyu Yang, Liuchang Jing, Wentao Li, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p1240-yang.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p1240-yang.pdf) `quantization`
- **Revisiting Filtered ANN Benchmarks: A Hardness-Controlled Benchmark Generator for Realistic Evaluation**<br>Mintaek Lim, Dogeun Kim, Minwoo Kim, Jaeyoung Do [[paper]](https://www.vldb.org/pvldb/vol19/p2763-lim.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p2763-lim.pdf) `filtered` `benchmark`
- **RNSG: A Range-Aware Graph Index for Efficient Range-Filtered Approximate Nearest Neighbor Search**<br>Zhiqiu Zou, Ziqi Yin, Rong-Hua Li, Hongchao Qin, Qiangqiang Dai, Guoren Wang [[paper]](https://www.vldb.org/pvldb/vol19/p2839-zou.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p2839-zou.pdf) `filtered`
- **Sparse Neighborhood Graph-Based Approximate Nearest Neighbor Search Revisited: Theoretical Analysis and Optimization**<br>Xinran Ma, Zhaoqi Zhou, Chuan Zhou, Zaijiu Shang, Guoliang Li, Zhiming Ma [[paper]](https://www.vldb.org/pvldb/vol19/p2817-zhou.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p2817-zhou.pdf) `graph` `theory`

#### MLSys 2026

- **When Enough is Enough: Rank-Aware Early Termination for Vector Search**<br>Jianan Lu, Asaf Cidon, Michael Freedman [[paper]](https://proceedings.mlsys.org/paper_files/paper/2026/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html) [[pdf]](https://proceedings.mlsys.org/paper_files/paper/2026/file/78834433edc3291f4c6cbbd2759324db-Paper-Conference.pdf) `early-termination`

#### SIGMOD 2025

- **DEG: Efficient Hybrid Vector Search Using the Dynamic Edge Navigation Graph**<br>Ziqi Yin, Jianyang Gao, Pasquale Balsebre, Gao Cong, Cheng Long [[paper]](https://doi.org/10.1145/3709679) [[arXiv]](https://arxiv.org/abs/2502.07343) `hybrid` `graph`
- **DIGRA: A Dynamic Graph Indexing for Approximate Nearest Neighbor Search with Range Filter**<br>Mengxu Jiang, Zhi Yang, Fangyuan Zhang, Guanhao Hou, Jieming Shi, Wenchao Zhou, et al. [[paper]](https://doi.org/10.1145/3725399) `filtered` `dynamic`
- **Efficient Dynamic Indexing for Range Filtered Approximate Nearest Neighbor Search**<br>Fangyuan Zhang, Mengxu Jiang, Guanhao Hou, Jieming Shi, Hua Fan, Wenchao Zhou, et al. [[paper]](https://doi.org/10.1145/3725401) `filtered` `dynamic`
- **Fast Approximate Similarity Join in Vector Databases**<br>Jiadong Xie, Jeffrey Xu Yu, Yingfan Liu [[paper]](https://doi.org/10.1145/3725403) `join`
- **Graph-Based Vector Search: An Experimental Evaluation of the State-of-the-Art**<br>Ilias Azizi, Karima Echihabi, Themis Palpanas [[paper]](https://doi.org/10.1145/3709693) [[arXiv]](https://arxiv.org/abs/2502.05575) `graph` `benchmark`
- **iRangeGraph: Improvising Range-dedicated Graphs for Range-filtering Nearest Neighbor Search**<br>Yuexuan Xu, Jianyang Gao, Yutong Gou, Cheng Long, Christian S. Jensen [[paper]](https://doi.org/10.1145/3698814) [[arXiv]](https://arxiv.org/abs/2409.02571) `filtered`
- **MIRAGE-ANNS: Mixed Approach Graph-based Indexing for Approximate Nearest Neighbor Search**<br>Sairaj Voruganti, M. Tamer Özsu [[paper]](https://doi.org/10.1145/3725325) `graph`
- **Navigating Labels and Vectors: A Unified Approach to Filtered Approximate Nearest Neighbor Search**<br>Yuzheng Cai, Jiayang Shi, Yizhuo Chen, Weiguo Zheng [[paper]](https://doi.org/10.1145/3698822) `filtered`
- **Practical and Asymptotically Optimal Quantization of High-Dimensional Vectors in Euclidean Space for Approximate Nearest Neighbor Search**<br>Jianyang Gao, Yutong Gou, Yuexuan Xu, Yongyi Yang, Cheng Long, Raymond Chi-Wing Wong [[paper]](https://doi.org/10.1145/3725413) [[arXiv]](https://arxiv.org/abs/2409.09913) `quantization`
- **RWalks: Random Walks as Attribute Diffusers for Filtered Vector Search**<br>Anas Ait Aomar, Karima Echihabi, Marco Arnaboldi, Ioannis Alagiannis, Damien Hilloulin, Manal Cherkaoui [[paper]](https://doi.org/10.1145/3725349) `filtered`
- **Subspace Collision: An Efficient and Accurate Framework for High-dimensional Approximate Nearest Neighbor Search**<br>Jiuqi Wei, Xiaodong Lee, Zhenyu Liao, Themis Palpanas, Botao Peng [[paper]](https://doi.org/10.1145/3709729) [[arXiv]](https://arxiv.org/abs/2411.14754)
- **SymphonyQG: Towards Symphonious Integration of Quantization and Graph for Approximate Nearest Neighbor Search**<br>Yutong Gou, Jianyang Gao, Yuexuan Xu, Cheng Long [[paper]](https://doi.org/10.1145/3709730) [[arXiv]](https://arxiv.org/abs/2411.12229) `graph` `quantization`

#### VLDB 2025

- **Accelerating Approximate Nearest Neighbor Search in Hierarchical Graphs: Efficient Level Navigation with Shortcuts**<br>Zengyang Gong, Yuxiang Zeng, Lei Chen [[paper]](https://www.vldb.org/pvldb/vol18/p3518-chen.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p3518-chen.pdf) `graph`
- **Cardinality Estimation for Similarity Search on High-Dimensional Data Objects: The Impact of Reference Objects**<br>Hai Lan, Shixun Huang, Zhifeng Bao, Renata Borovica-Gajic [[paper]](https://www.vldb.org/pvldb/vol18/p544-bao.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p544-bao.pdf)
- **Cracking Vector Search Indexes**<br>Vasilis Mageirakos, Bowen Wu, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p3951-mageirakos.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p3951-mageirakos.pdf) `adaptive`
- **Dynamic Range-Filtering Approximate Nearest Neighbor Search**<br>Zhencan Peng, Miao Qiao, Wenchao Zhou, Feifei Li, Dong Deng [[paper]](https://www.vldb.org/pvldb/vol18/p3256-deng.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p3256-deng.pdf) `filtered` `dynamic`
- **Efficient Data-aware Distance Comparison Operations for High-Dimensional Approximate Nearest Neighbor Search**<br>Liwei Deng, Penghao Chen, Ximu Zeng, Tianfu Wang, Yan Zhao, Kai Zheng [[paper]](https://www.vldb.org/pvldb/vol18/p812-zheng.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p812-zheng.pdf)
- **Filtered Vector Search: State-of-the-art and Research Challenges**<br>Helena Caminal, Yannis Chronis, Yannis Papakonstantinou, Fatma Özcan, Anastasia Ailamaki [[paper]](https://www.vldb.org/pvldb/vol18/p5488-caminal.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p5488-caminal.pdf) `filtered` `survey`
- **GTI: Graph-based Tree Index with Logarithm Updates for Nearest Neighbor Search in High-Dimensional Spaces**<br>Ruiyao Ma, Yifan Zhu, Baihua Zheng, Lu Chen, Congcong Ge, Yunjun Gao [[paper]](https://www.vldb.org/pvldb/vol18/p986-gao.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p986-gao.pdf) `dynamic`
- **Maximum Inner Product is Query-Scaled Nearest Neighbor**<br>Tingyang Chen, Cong Fu, Kun Wang, Xiangyu Ke, Yunjun Gao, Wenchao Zhou, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p1770-ke.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p1770-ke.pdf) `mips`
- **Not Small Enough? SegPQ: A Learned Approach to Compress Product Quantization Codebooks**<br>Qiyu Liu, Yanlin Qi, Siyuan Han, Jingshu Peng, Jin Li, Lei Chen [[paper]](https://www.vldb.org/pvldb/vol18/p3730-liu.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p3730-liu.pdf) `quantization`
- **Revisiting the Index Construction of Proximity Graph-Based Approximate Nearest Neighbor Search**<br>Shuo Yang, Jiadong Xie, Yingfan Liu, Jeffrey Xu Yu, Xiyue Gao, Qianru Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p1825-liu.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p1825-liu.pdf) `graph`
- **SIEVE: Effective Filtered Vector Search with Collection of Indexes**<br>Zhaoheng Li, Silu Huang, Wei Ding, Yongjoo Park, Jianjun Chen [[paper]](https://www.vldb.org/pvldb/vol18/p4723-li.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p4723-li.pdf) `filtered`
- **UNIFY: Unified Index for Range Filtered Approximate Nearest Neighbors Search**<br>Anqi Liang, Pengcheng Zhang, Bin Yao, Zhongpu Chen, Yitong Song, Guangxu Cheng [[paper]](https://www.vldb.org/pvldb/vol18/p1118-yao.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p1118-yao.pdf) `filtered`
- **Wolverine: Highly Efficient Monotonic Search Path Repair for Graph-based ANN Index Updates**<br>Dawei Liu, Bolong Zheng, Ziyang Yue, Fuhao Ruan, Xiaofang Zhou, Christian S. Jensen [[paper]](https://www.vldb.org/pvldb/vol18/p2268-zheng.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p2268-zheng.pdf) `graph` `dynamic`

#### PPoPP 2025

- **PANNS: Enhancing Graph-based Approximate Nearest Neighbor Search through Recency-aware Construction and Parameterized Search**<br>Xizhe Yin, Chao Gao, Zhijia Zhao, et al. [[paper]](https://doi.org/10.1145/3710848.3710867) `graph`

### Systems

_Vector databases, disk/SSD-resident and distributed search, updates, DBMS integration, privacy, and retrieval for RAG / KV cache._

#### OSDI 2026

- **The Clustering Strikes Back: Building Cost-Effective and High-Performance ANNS at Scale with Helmsman (Operational Systems)**<br>Yuchen Huang, Baiteng Ma, Yiping Sun, Yang Shi, Xiao Chen, Xiaocheng Zhong, et al. [[paper]](https://www.usenix.org/conference/osdi26/presentation/huang-yuchen) [[pdf]](https://www.usenix.org/system/files/osdi26-huang-yuchen.pdf) `partition` `disk`

#### SIGMOD 2026

- **An In-Depth Study of Filter-Agnostic Vector Search on a PostgreSQL Database System: [Experiments & Analysis]**<br>Duo Lu, Helena Caminal, Manos Chatzakis, Yannis Papakonstantinou, Yannis Chronis, Vaibhav Jain, et al. [[paper]](https://doi.org/10.1145/3802011) [[arXiv]](https://arxiv.org/abs/2603.23710) `filtered` `postgres` `benchmark`
- **Building Stateless Serverless Vector DBs via Block-based Data Partitioning**<br>Daniel Barcelona Pons, Raúl Gracia Tinedo, Albert Cañadilla-Domingo, Xavier Roca-Canals, Pedro García López [[paper]](https://doi.org/10.1145/3769769) `serverless`
- **CoTra: Towards Efficient and Scalable Distributed Vector Search with RDMA**<br>Xiangyu Zhi, Meng Chen, Xiao Yan, Baotong Lu, Hui Li, Qianxi Zhang, et al. [[paper]](https://doi.org/10.1145/3786634) [[arXiv]](https://arxiv.org/abs/2507.06653) `distributed` `rdma`
- **DiskJoin: Large-scale Vector Similarity Join with SSD**<br>Yanqi Chen, Xiao Yan, Alexandra Meliou, Eric Lo [[paper]](https://doi.org/10.1145/3769780) [[arXiv]](https://arxiv.org/abs/2508.18494) `disk` `join`
- **Efficient Index Layout and Search Strategy for Large-scale High-dimensional Vector Similarity Search**<br>Weijian Chen, Haotian Liu, Yangshen Deng, Long Xiang, Liang Huang, Bo Tang [[paper]](https://doi.org/10.1145/3802045) `disk`
- **GPS: Revisiting the Data Layout for Disk-based High-Dimensional Vector Search**<br>Peiqi Yin, Xiao Yan, Qihui Zhou, Hui Li, Xiaolu Li, Meiling Wang, et al. [[paper]](https://doi.org/10.1145/3802069) `disk`
- **HARMONY: A Scalable Distributed Vector Database for High-Throughput Approximate Nearest Neighbor Search**<br>Qian Xu, Feng Zhang, Chengxi Li, Lei Cao, Zheng Chen, Jidong Zhai, et al. [[paper]](https://doi.org/10.1145/3749167) [[arXiv]](https://arxiv.org/abs/2506.14707) `distributed`
- **HONEYBEE: Efficient Role-based Access Control for Vector Databases via Dynamic Partitioning**<br>Hongbin Zhong, Matthew Lentz, Nina Narodytska, Adriana Szekeres, Kexin Rong [[paper]](https://doi.org/10.1145/3786625) [[arXiv]](https://arxiv.org/abs/2505.01538) `privacy` `access-control`
- **Integrating Vector Databases across Embedding Models**<br>Beining Yang, Yang Cao, Yang Ren [[paper]](https://doi.org/10.1145/3769803) `embedding-models`

#### VLDB 2026

- **Aker: Density-Aware Approximate Caching for Vector Search**<br>Sukjoon Oh, Minki Kang, Dohyun Kim, Baotong Lu, Jing Liu, Qianxi Zhang, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p2727-oh.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p2727-oh.pdf) `caching`
- **Balancing the Blend: An Experimental Analysis of Trade-offs in Hybrid Search**<br>Mengzhao Wang, Boyu Tan, Yunjun Gao, Hai Jin, Yingfeng Zhang, Xiangyu Ke, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1715-gao.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p1715-gao.pdf) `hybrid` `benchmark`
- **FedBridge: A Federated Query Engine over Embedding-Heterogeneous Vector Databases**<br>Yuxiang Wang, Ruixi Hu, Ziyuan He, Zhilin Liang, Xinyu Zhao, Yongxin Tong [[paper]](https://www.vldb.org/pvldb/vol19/p4498-tong.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p4498-tong.pdf) `federated`
- **I/O Optimizations in Graph-Based Disk-Resident Approximate Nearest Neighbor Search: A Design Space Exploration**<br>Liang Li, Shufeng Gong, Yanan Yang, Yiduo Wang, Jie Wu [[paper]](https://www.vldb.org/pvldb/vol19/p1484-li.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p1484-li.pdf) `disk` `benchmark`
- **Nova: A Multi-Purpose Vector Engine for Low-Latency, Multi-Tenant, and Cross-Table Hybrid Retrieval**<br>Dechuang Chen, Bing Chen, Jianwei Lu, Zhiwei Wu, Zeyu Yang, Qiang Gu, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p4453-zhou.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p4453-zhou.pdf) `hybrid` `vector-db`
- **RED-ANNS: A RDMA-Enabled Distributed Framework for Graph-Based Approximate Nearest Neighbor Search**<br>Yue Chen, Kai Zhang, Sipeng Chen, Shihai Xiao, Xiaomin Zou, Ren Ren, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p399-chen.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p399-chen.pdf) `distributed` `rdma` `graph`
- **RetroInfer: A Vector Storage Engine for Scalable Long-Context LLM Inference**<br>Yaoqi Chen, Jinkai Zhang, Baotong Lu, Qianxi Zhang, Chengruidong Zhang, Jing Liu, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1016-lu.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p1016-lu.pdf) `kvcache`
- **SQL-Native Vector Search at Billion Scale in Presto**<br>Zhichen Xu, Ge Gao, Ke Wang, Aakash Deep, Junjie Qi, Jort Gemmeke, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p4182-xu.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p4182-xu.pdf) `vector-db`
- **TEngineDB-V: An OLAP-Native Vector Search System for Large-𝑘 Workloads at Tencent**<br>Xufei Wu, Pengcheng Zhang, Yitong Song, Xiaobo Zhang, Anqi Liang, Kai Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p3955-zhou.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3955-zhou.pdf) `vector-db`
- **V3DB: Audit-on-Demand Zero-Knowledge Proofs for Verifiable Vector Search over Committed Snapshots**<br>Zipeng Qiu, Wenjie Qu, Jiaheng Zhang, Binhang Yuan [[paper]](https://www.vldb.org/pvldb/vol19/p2604-qiu.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p2604-qiu.pdf) `zkp` `verifiable`

#### MLSys 2026

- **LEANN: A Low-Storage Overhead Vector Index**<br>Yichuan Wang, Zhifei Li, Shu Liu, Yongji Wu, Ziming Mao, Yilong Zhao, et al. [[paper]](https://proceedings.mlsys.org/paper_files/paper/2026/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) [[pdf]](https://proceedings.mlsys.org/paper_files/paper/2026/file/e27ea0cd50b798ff8942caf9203f0992-Paper-Conference.pdf) `storage` `graph`
- **TeleRAG: Efficient Retrieval-Augmented Generation Inference with Lookahead Retrieval**<br>Chien-Yu Lin, Keisuke Kamahori, Yiyu Liu, Xiaoxiang Shi, Madhav Kashyap, Yile Gu, et al. [[paper]](https://proceedings.mlsys.org/paper_files/paper/2026/hash/7fd522b89ac21009b7bbe7560a9a5add-Abstract-Conference.html) [[pdf]](https://proceedings.mlsys.org/paper_files/paper/2026/file/7fd522b89ac21009b7bbe7560a9a5add-Paper-Conference.pdf) `rag` `gpu`

#### HPCA 2026

- **VectorLiteRAG: Latency-Aware and Fine-Grained Resource Partitioning for Efficient RAG**<br>Junkyum Kim, Divya Mahajan [[paper]](https://doi.org/10.1109/HPCA68181.2026.11408552) [[arXiv]](https://arxiv.org/abs/2504.08930) `rag` `gpu` `ivf`

#### OSDI 2025

- **Achieving Low-Latency Graph-Based Vector Search via Aligning Best-First Search Algorithm with SSD**<br>Hao Guo, Youyou Lu [[paper]](https://www.usenix.org/conference/osdi25/presentation/guo) [[pdf]](https://www.usenix.org/system/files/osdi25-guo.pdf) `disk` `graph`
- **Compass: Encrypted Semantic Search with High Accuracy**<br>Jinhao Zhu, Liana Patel, Matei Zaharia, Raluca Ada Popa [[paper]](https://www.usenix.org/conference/osdi25/presentation/zhu-jinhao) [[pdf]](https://www.usenix.org/system/files/osdi25-zhu-jinhao.pdf) `privacy`
- **Quake: Adaptive Indexing for Vector Search**<br>Jason Mohoney, Devesh Sarda, Mengze Tang, Shihabur Rahman Chowdhury, Anil Pacaci, Ihab F. Ilyas, et al. [[paper]](https://www.usenix.org/conference/osdi25/presentation/mohoney) [[pdf]](https://www.usenix.org/system/files/osdi25-mohoney.pdf) `dynamic` `partition`

#### SIGMOD 2025

- **Accelerating Graph Indexing for ANNS on Modern CPUs**<br>Mengzhao Wang, Haotian Wu, Xiangyu Ke, Yunjun Gao, Yifan Zhu, Wenchao Zhou [[paper]](https://doi.org/10.1145/3725260) [[arXiv]](https://arxiv.org/abs/2502.18113) `graph` `cpu`
- **PDX: A Data Layout for Vector Similarity Search**<br>Leonardo Kuffó, Elena Krippner, Peter Boncz [[paper]](https://doi.org/10.1145/3725333) [[arXiv]](https://arxiv.org/abs/2503.04422) `layout`
- **PQCache: Product Quantization-based KVCache for Long Context LLM Inference**<br>Hailin Zhang, Xiaodong Ji, Yilin Chen, Fangcheng Fu, Xupeng Miao, Xiaonan Nie, et al. [[paper]](https://doi.org/10.1145/3725338) [[arXiv]](https://arxiv.org/abs/2407.12820) `kvcache` `quantization`
- **Tribase: A Vector Data Query Engine for Reliable and Lossless Pruning Compression using Triangle Inequalities**<br>Qian Xu, Juan Yang, Feng Zhang, Junda Pan, Kang Chen, Youren Shen, et al. [[paper]](https://doi.org/10.1145/3709743)

#### VLDB 2025

- **BigVectorBench: Heterogeneous Data Embedding and Compound Queries are Essential in Evaluating Vector Databases**<br>Guoxin Kang, Zhongxin Ge, Jingpei Hu, Xueya Zhang, Lei Wang, Jianfeng Zhan [[paper]](https://www.vldb.org/pvldb/vol18/p1536-zhan.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p1536-zhan.pdf) `benchmark`
- **Cost-Effective, Low Latency Vector Search with Azure Cosmos DB**<br>Nitish Upreti, Harsha Vardhan Simhadri, Hari Sudan Sundar, Krishnan Sundaram, Samer Boshra, Balachandar Perumalswamy, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p5166-upreti.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p5166-upreti.pdf) `vector-db` `cloud`
- **FedVSE: A Privacy-Preserving and Efficient Vector Search Engine for Federated Databases**<br>Zeheng Fan, Yuxiang Zeng, Zhuanglin Zheng, Yongxin Tong [[paper]](https://www.vldb.org/pvldb/vol18/p5371-tong.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p5371-tong.pdf) `privacy` `federated`
- **GaussDB-Vector: A Large-Scale Persistent Real-Time Vector Database for LLM Applications**<br>Guoliang Li, Ji Sun, James Pan, Jiang Wang, Yongqing Xie, Ruicheng Liu, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p4951-sun.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p4951-sun.pdf) `vector-db`
- **HAKES: Scalable Vector Database for Embedding Search Service**<br>Guoyu Hu, Shaofeng Cai, Tien Tuan Anh Dinh, Zhongle Xie, Cong Yue, Gang Chen, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p3049-ooi.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p3049-ooi.pdf) `distributed`
- **NaviX: A Native Vector Index Design for Graph DBMSs With Robust Predicate-Agnostic Search Performance**<br>Gaurav Sehgal, Semih Salihoglu [[paper]](https://www.vldb.org/pvldb/vol18/p4438-sehgal.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p4438-sehgal.pdf) `filtered` `graph-dbms`
- **Select Edges Wisely: Monotonic Path Aware Graph Layout Optimization for Disk-based ANN Search**<br>Ziyang Yue, Bolong Zheng, Ling Xu, Kanru Xu, Shuhao Zhang, Yajuan Du, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p4337-zheng.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p4337-zheng.pdf) `disk` `graph`
- **Turbocharging Vector Databases using Modern SSDs**<br>Joobo Shim, Jaewon Oh, Hongchan Roh, Jaeyoung Do, Sang-Won Lee [[paper]](https://www.vldb.org/pvldb/vol18/p4710-do.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p4710-do.pdf) `disk`
- **Unleashing Graph Partitioning for Large-Scale Nearest Neighbor Search**<br>Lars Gottesbüren, Laxman Dhulipala, Rajesh Jayaram, Jakub Lacki [[paper]](https://www.vldb.org/pvldb/vol18/p1649-gottesbueren.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p1649-gottesbueren.pdf) `distributed` `partition`
- **VSAG: An Optimized Search Framework for Graph-based Approximate Nearest Neighbor Search**<br>Xiaoyao Zhong, Haotian Li, Jiabao Jin, Mingyu Yang, Deming Chu, Xiangyu Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p5017-cheng.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p5017-cheng.pdf) `graph`
- **VStream: A Distributed Streaming Vector Search System**<br>Shenghao Gong, Haobo Sun, Ziquan Fang, Liu Liu, Lu Chen, Yunjun Gao [[paper]](https://www.vldb.org/pvldb/vol18/p1593-gao.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p1593-gao.pdf) `distributed` `dynamic`

#### ISCA 2025

- **Hermes: Algorithm-System Co-design for Efficient Retrieval-Augmented Generation At-Scale**<br>Michael Shen, Muhammad Umar, Kiwan Maeng, et al. [[paper]](https://pure.psu.edu/en/publications/hermes-algorithm-system-co-design-for-efficient-retrieval-augment/) `rag` `distributed`
- **RAGO: Systematic Performance Optimization for Retrieval-Augmented Generation Serving**<br>Wenqi Jiang, Suvinay Subramanian, Cat Graves, et al. [[paper]](https://doi.org/10.1145/3695053.3731093) [[arXiv]](https://arxiv.org/abs/2503.14649) [[code]](https://github.com/google/rago) `rag`

### Accelerators

_GPU, FPGA, ASIC, processing-in/near-memory, in-storage, and CXL-based vector search._

#### OSDI 2026

- **Disentangling Graph Dependencies for Efficient Billion-Scale GPU Vector Search**<br>Haoru Zhao, Jingkai He, Jingyao Zeng, Mingkai Dong, Dong Du [[paper]](https://www.usenix.org/conference/osdi26/presentation/zhao) [[pdf]](https://www.usenix.org/system/files/osdi26-zhao.pdf) `gpu` `graph`

#### SIGMOD 2026

- **CMANNS: GPU-Accelerated Graph Index Construction for ANNS via Compute-Memory Disaggregation**<br>Chengying Huan, Renjie Yao, Shaonan Ma, Rong Gu, Zhengyi Yang, Lizheng Chen, et al. [[paper]](https://doi.org/10.1145/3802027) `gpu` `graph`
- **FlashANNS: GPU-Driven Asynchronous I/O Pipelining for Eliminating Storage-Compute Bottlenecks in Billion-Scale Similarity Search**<br>Yang Xiao, Mo Sun, Ziyu Song, Bing Tian, Jie Sun, Jie Zhang, et al. [[paper]](https://doi.org/10.1145/3786652) `gpu` `disk`
- **High-Throughput, Cost-Effective Billion-Scale Vector Search with a Single GPU**<br>Haodi Jiang, Hao Guo, Minhui Xie, Jiwu Shu, Youyou Lu [[paper]](https://doi.org/10.1145/3769799) `gpu` `billion-scale`
- **Scalable Graph Indexing using GPUs for Approximate Nearest Neighbor Search**<br>Zhonggen Li, Xiangyu Ke, Yifan Zhu, Bocheng Yu, Baihua Zheng, Yunjun Gao [[paper]](https://doi.org/10.1145/3769825) [[arXiv]](https://arxiv.org/abs/2508.08744) `gpu` `graph`
- **VecFlow-Chamfer: A GPU-based Data Management System for High-Performance Multi-Vector Search on Superchips**<br>Chenghao Mo, Ben Karsin, Philip Adams, Minjia Zhang [[paper]](https://doi.org/10.1145/3786706) `gpu` `multi-vector`
- **VecFlow: A High-Performance Vector Data Management System for Filtered-Search on GPUs**<br>Jingyi Xi, Chenghao Mo, Ben Karsin, Artem M. Chirkin, Mingqin Li, Minjia Zhang [[paper]](https://doi.org/10.1145/3749189) [[arXiv]](https://arxiv.org/abs/2506.00812) `gpu` `filtered`

#### VLDB 2026

- **GPU-Accelerated ANNS: Quantized for Speed, Built for Change**<br>Hunter McCoy, Zikun Wang, Prashant Pandey [[paper]](https://www.vldb.org/pvldb/vol19/p3413-pandey.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3413-pandey.pdf) `gpu` `quantization` `dynamic`
- **GPU-Native Approximate Nearest Neighbor Search with IVF-RaBitQ: Fast Index Build and Search**<br>Jifan Shi, Jianyang Gao, James Xia, Tamas B. Fehér, Cheng Long [[paper]](https://www.vldb.org/pvldb/vol19/p3454-shi.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p3454-shi.pdf) `gpu` `quantization`
- **SVFusion: A CPU-GPU Co-Processing Architecture for Large-Scale Real-Time Vector Search**<br>Yuchen Peng, Dingyu Yang, Zhongle Xie, Ji Sun, Lidan Shou, Ke Chen, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1074-yang.pdf) [[pdf]](https://www.vldb.org/pvldb/vol19/p1074-yang.pdf) `gpu` `dynamic`

#### ISCA 2026

- **NasZip: Software and Hardware Co-design to Accelerate Approximate Nearest Neighbor Search with DIMM-based Near-Data Processing**<br>Cheng Zou, S. Yang, C. Nie, et al. [[paper]](https://doi.org/10.1109/ISCA66397.2026.00105) [[arXiv]](https://arxiv.org/abs/2605.21952) [[code]](https://github.com/Intelligent-Computing-Research-Group/NasZip) `near-memory` `early-termination` `graph`

#### MICRO 2026

- **D-NOVA: In-Storage Retrieval Accelerator via Dual-Bound 3D NAND-Optimized Similarity Search with Vector Adaptation** *(accepted, to appear)*<br>Chang Eun Song, Sumukh Pinge, Tianqi Zhang, et al. [[arXiv]](https://arxiv.org/abs/2607.17538) `in-storage` `in-flash` `ivf` `rag`<br><sub>Listed in the MICRO 2026 program (Session 9B).</sub>
- **MFNNS: A Multiplier-Free Near-Memory Accelerator for Graph-based ANNS** *(accepted, to appear)*<br>Rui Meng, Yonghao Chen, Jiaxiang Zou, et al. `near-memory` `graph`<br><sub>Listed in the MICRO 2026 program (Session 9B).</sub>
- **NiF: Hybrid In-Flash and In-Storage Acceleration for Approximate Nearest Neighbor Search** *(accepted, to appear)*<br>Myoungjun Chun, et al. `in-storage` `in-flash`<br><sub>Listed in the MICRO 2026 program (Session 4A).</sub>
- **WiFlash: Wordline-Parallel Approximate Nearest Neighbor Search Inside Flash Cell Array** *(accepted, to appear)*<br>Hyunjin Kim, Juchan Lee, Inseong Choi, et al. `in-flash`<br><sub>Listed in the MICRO 2026 program (Session 9B).</sub>

#### SC 2026

- **PIMCQG: Co-Designing Billion-Scale Graph-Based Approximate Nearest Neighbor Search for Processing-in-Memory** *(accepted, to appear)*<br>Sitian Chen, Yusen Li, Yao Chen, et al. [[arXiv]](https://arxiv.org/abs/2605.25522) [[code]](https://github.com/steam009/PIMCQG) `pim` `graph` `quantization` `billion-scale`<br><sub>Acceptance per the code README and <a href="https://amelieczhou.github.io/publications.html">author homepage</a>.</sub>

#### ASPLOS 2025

- **Accelerating Retrieval-Augmented Generation**<br>Derrick Quinn, Mohammad Nouri, Neel Patel, John Salihu, Alireza Salemi, Sukhan Lee, et al. [[paper]](https://doi.org/10.1145/3669940.3707264) [[arXiv]](https://arxiv.org/abs/2412.15246) `rag` `near-memory`

#### VLDB 2025

- **Chameleon: a Heterogeneous and Disaggregated Accelerator System for Retrieval-Augmented Language Models**<br>Wenqi Jiang, Marco Zeller, Roger Waleffe, Torsten Hoefler, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p42-jiang.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p42-jiang.pdf) `rag` `disaggregated`
- **Fast Graph Vector Search via Hardware Acceleration and Delayed-Synchronization Traversal**<br>Wenqi Jiang, Hang Hu, Torsten Hoefler, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p3797-jiang.pdf) [[pdf]](https://www.vldb.org/pvldb/vol18/p3797-jiang.pdf) `fpga` `graph`

#### ISCA 2025

- **ANSMET: Approximate Nearest Neighbor Search with Near-Memory Processing and Hybrid Early Termination**<br>Yiwei Li, Yuxin Jin, Boyu Tian, et al. [[paper]](https://doi.org/10.1145/3695053.3731013) [[pdf]](https://people.iiis.tsinghua.edu.cn/~gaomy/pubs/ansmet.isca25.pdf) `near-memory` `early-termination`
- **DReX: Accurate and Scalable Dense Retrieval Acceleration via Algorithmic-Hardware Codesign**<br>Derrick Quinn, E. Ezgi Yücel, Martin Prammer, et al. [[paper]](https://par.nsf.gov/biblio/10634219) `near-memory` `rag`
- **HeterRAG: Heterogeneous Processing-in-Memory Acceleration for Retrieval-augmented Generation**<br>Chaoqiang Liu, Haifeng Liu, Dan Chen, et al. `pim` `rag`
- **In-Storage Acceleration of Retrieval Augmented Generation as a Service**<br>Rohan Mahapatra, Harsha Santhanam, Christopher Priebe, et al. [[paper]](https://doi.org/10.1145/3695053.3731032) `in-storage` `rag`
- **REIS: A High-Performance and Energy-Efficient Retrieval System with In-Storage Processing**<br>Kangqi Chen, Andreas Kosmas Kakolyris, Rakesh Nadig, Manos Frouzakis, et al. [[arXiv]](https://arxiv.org/abs/2506.16444) `in-storage` `ivf` `rag`

#### MICRO 2025

- **Accelerating Retrieval Augmented Language Model via PIM and PNM Integration**<br>Je-Woo Jang, Junyong Oh, et al. [[paper]](https://doi.org/10.1145/3725843.3756020) `pim` `near-memory` `ivf` `quantization` `rag`
- **Characterizing and Optimizing Realistic Workloads on a Commercial Compute-in-SRAM Device**<br>Niansong Zhang, Wenbo Zhu, Courtney Golden, et al. [[paper]](https://doi.org/10.1145/3725843.3756132) [[arXiv]](https://arxiv.org/abs/2509.05451) `compute-in-sram` `rag`<br><sub>Characterization paper; its main case study is RAG retrieval on the GSI APU.</sub>

#### HPCA 2025

- **AccelES: Accelerating Top-K SpMV for Embedding Similarity via Low-bit Pruning**<br>Jiaqi Zhai, Xuanhua Shi, Kaiyi Huang, et al. [[paper]](https://doi.org/10.1109/HPCA61900.2025.00077) `exact-search` `sparse`<br><sub>Exact (not approximate) top-K embedding similarity search; adjacent to ANNS.</sub>
- **NeuVSA: A Unified and Efficient Accelerator for Neural Vector Search**<br>Ziming Yuan, Lei Dai, Wen Li, et al. [[paper]](https://doi.org/10.1109/HPCA61900.2025.00065) `quantization` `learned`

#### SC 2025

- **DRIM-ANN: An Approximate Nearest Neighbor Search Engine based on Commercial DRAM-PIMs**<br>Mingkai Chen, Tianhua Han, Cheng Liu, et al. [[paper]](https://doi.org/10.1145/3712285.3759801) [[arXiv]](https://arxiv.org/abs/2410.15621) `pim` `ivf` `quantization`
- **UpANNS: Enhancing Billion-Scale ANNS Efficiency with Real-World PIM Architecture**<br>Sitian Chen, Amelie Chi Zhou, Yucheng Shi, et al. [[paper]](https://doi.org/10.1145/3712285.3759777) [[arXiv]](https://arxiv.org/abs/2410.23805) `pim` `ivf` `quantization` `billion-scale`
<!-- END GENERATED -->
