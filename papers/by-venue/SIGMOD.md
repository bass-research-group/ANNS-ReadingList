# SIGMOD

ANNS and vector search papers at SIGMOD, all years. Generated from [`data/papers/`](../../data/papers/); edit those files, not this one.

## SIGMOD 2027

### ANNS Indexing Algorithms

- **Amora: Communication-Efficient Private Approximate Nearest Neighbors Search** *(accepted, to appear)*<br>Qiuhao Wang, Zuowei Chen, Xu Yang, et al. [[code]](https://github.com/meander-wqh/Amora) `privacy`
- **Exploiting Structural Properties for Efficient Constraint-Aware HNSW Hyperparameter Tuning** *(accepted, to appear)*<br>Geon Choi, Hoeun Lee, Jaeyoung Do [[arXiv]](https://arxiv.org/abs/2607.04630) [[code]](https://github.com/AIDASLab/CHAT) `graph` `tuning`<br><sub>SIGMOD 2027 round 1 (<a href="https://aidas.snu.ac.kr/news/2026-06-13-1-paper-has-been-accepted-to-sigmod-2027/">lab news</a>).</sub>
- **Reverse Neighbor Sliding and Order Selection for Efficient Multi-Proximity Graph Merging** *(accepted, to appear)*<br>Liuchang Jing, Mingyu Yang, Lei Li, et al. [[arXiv]](https://arxiv.org/abs/2602.17099) [[code]](https://github.com/JingLiuchang/hnsw-merge) `graph` `merging`<br><sub>arXiv v1 title: "Multiple Index Merge for Approximate Nearest Neighbor Search".</sub>

### Filtered ANNS Algorithms

- **Fast Label-Filtering Approximate Nearest Neighbor Search via Progressive Label Set Stratification** *(accepted, to appear)*<br>Ziqi Wang, Jingzhe Zhang, Shuo Shen, et al. [[arXiv]](https://arxiv.org/abs/2609.15058)

### GPU-Accelerated ANNS Systems

- **All-in-One Graph-Based Indexing for Hybrid Search on GPUs** *(accepted, to appear)*<br>Zhonggen Li, Yougen Li, Yifan Zhu, et al. [[arXiv]](https://arxiv.org/abs/2511.00855) `graph` `hybrid`

### Vector Databases & Other Systems

- **Catching Inconsistencies in Vector Similarity Retrieval** *(accepted, to appear)*<br>Zixiao Huang, Ruochun Jin, Haotian Wang, et al. `testing` `vector-db`<br><sub>SIGMOD 2027 round 2, per the author's publication page.</sub>
- **Metric Algebra: Embedding-Independence in Vector Databases** *(accepted, to appear)*<br>University of Edinburgh authors (to be filled in) `embedding-models`<br><sub>Listed in the SIGMOD 2027 round 1 accepted papers.</sub>

## SIGMOD 2026

### ANNS Indexing Algorithms

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

### Filtered ANNS Algorithms

- **Beyond Vector Search: Querying With and Without Predicates**<br>Jiadong Xie, Jeffrey Xu Yu, Siyi Teng, Yingfan Liu [[paper]](https://doi.org/10.1145/3769765)
- **Curator: Efficient Vector Search with Low-Selectivity Filters**<br>Yicheng Jin, Yongji Wu, Wenjun Hu, Bruce M. Maggs, Jun Yang, Xiao Zhang, et al. [[paper]](https://doi.org/10.1145/3786635) [[arXiv]](https://arxiv.org/abs/2601.01291) [[code]](https://github.com/hatsu3/curator-v2)
- **FAVOR: Efficient Filter-Agnostic Vector ANNS Based on Selectivity-Aware Exclusion Distances**<br>Junjie Song, Yu Liu, Guoyu Hu, Zhongle Xie, Ming Yang, Beng Chin Ooi, et al. [[paper]](https://doi.org/10.1145/3802060) [[arXiv]](https://arxiv.org/abs/2605.07770)
- **PathSeer: Adaptive Neighbor Handling for Efficient Filtered ANN Search**<br>Zhiyue Li, Guangyan Zhang, Ruochun Jin, Bojun Li, Xiaoguang Ren, Wenjing Yang [[paper]](https://doi.org/10.1145/3802098) [[code]](https://github.com/lizhiyuell/PathSeer)
- **WoW: A Window-to-Window Incremental Index for Range-Filtering Approximate Nearest Neighbor Search**<br>Ziqi Wang, Jingzhe Zhang, Wei Hu [[paper]](https://doi.org/10.1145/3769843) [[arXiv]](https://arxiv.org/abs/2508.18617) [[code]](https://github.com/nju-websoft/WoW)

### Hybrid Search Algorithms

- **GEM: A Native Graph-based Index for Multi-Vector Retrieval**<br>Yao Tian, Zhoujin Tian, Xi Zhao, Ruiyuan Zhang, Xiaofang Zhou [[paper]](https://doi.org/10.1145/3802065) [[arXiv]](https://arxiv.org/abs/2603.20336) `multi-vector` `graph`

### GPU-Accelerated ANNS Systems

- **CMANNS: GPU-Accelerated Graph Index Construction for ANNS via Compute-Memory Disaggregation**<br>Chengying Huan, Renjie Yao, Shaonan Ma, Rong Gu, Zhengyi Yang, Lizheng Chen, et al. [[paper]](https://doi.org/10.1145/3802027) `graph`
- **FlashANNS: GPU-Driven Asynchronous I/O Pipelining for Eliminating Storage-Compute Bottlenecks in Billion-Scale Similarity Search**<br>Yang Xiao, Mo Sun, Ziyu Song, Bing Tian, Jie Sun, Jie Zhang, et al. [[paper]](https://doi.org/10.1145/3786652) [[code]](https://github.com/Tinkerver/ann_search) `disk`
- **High-Throughput, Cost-Effective Billion-Scale Vector Search with a Single GPU**<br>Haodi Jiang, Hao Guo, Minhui Xie, Jiwu Shu, Youyou Lu [[paper]](https://doi.org/10.1145/3769799) [[code]](https://github.com/thustorage/GustANN) `billion-scale`
- **Scalable Graph Indexing using GPUs for Approximate Nearest Neighbor Search**<br>Zhonggen Li, Xiangyu Ke, Yifan Zhu, Bocheng Yu, Baihua Zheng, Yunjun Gao [[paper]](https://doi.org/10.1145/3769825) [[arXiv]](https://arxiv.org/abs/2508.08744) [[code]](https://github.com/ZJU-DAILY/Tagore) `graph`
- **VecFlow-Chamfer: A GPU-based Data Management System for High-Performance Multi-Vector Search on Superchips**<br>Chenghao Mo, Ben Karsin, Philip Adams, Minjia Zhang [[paper]](https://doi.org/10.1145/3786706) [[code]](https://github.com/Supercomputing-System-AI-Lab/VecFlow) `multi-vector`
- **VecFlow: A High-Performance Vector Data Management System for Filtered-Search on GPUs**<br>Jingyi Xi, Chenghao Mo, Ben Karsin, Artem M. Chirkin, Mingqin Li, Minjia Zhang [[paper]](https://doi.org/10.1145/3749189) [[arXiv]](https://arxiv.org/abs/2506.00812) [[code]](https://github.com/Supercomputing-System-AI-Lab/VecFlow)

### Out-of-Core ANNS Systems

- **DiskJoin: Large-scale Vector Similarity Join with SSD**<br>Yanqi Chen, Xiao Yan, Alexandra Meliou, Eric Lo [[paper]](https://doi.org/10.1145/3769780) [[arXiv]](https://arxiv.org/abs/2508.18494) [[code]](https://github.com/iidyc/DiskJoin) `disk` `join`
- **Efficient Index Layout and Search Strategy for Large-scale High-dimensional Vector Similarity Search**<br>Weijian Chen, Haotian Liu, Yangshen Deng, Long Xiang, Liang Huang, Bo Tang [[paper]](https://doi.org/10.1145/3802045) [[code]](https://github.com/AlayaDB-AI/AlayaLite) `disk`
- **GPS: Revisiting the Data Layout for Disk-based High-Dimensional Vector Search**<br>Peiqi Yin, Xiao Yan, Qihui Zhou, Hui Li, Xiaolu Li, Meiling Wang, et al. [[paper]](https://doi.org/10.1145/3802069) [[code]](https://github.com/yinpeiqi/Gorgeous) `disk`

### Distributed ANNS Systems

- **CoTra: Towards Efficient and Scalable Distributed Vector Search with RDMA**<br>Xiangyu Zhi, Meng Chen, Xiao Yan, Baotong Lu, Hui Li, Qianxi Zhang, et al. [[paper]](https://doi.org/10.1145/3786634) [[arXiv]](https://arxiv.org/abs/2507.06653) [[code]](https://github.com/xiangyuzhi/CoTra) `rdma`
- **HARMONY: A Scalable Distributed Vector Database for High-Throughput Approximate Nearest Neighbor Search**<br>Qian Xu, Feng Zhang, Chengxi Li, Lei Cao, Zheng Chen, Jidong Zhai, et al. [[paper]](https://doi.org/10.1145/3749167) [[arXiv]](https://arxiv.org/abs/2506.14707) [[code]](https://github.com/xuqianmamba/Harmony)

### Vector Databases & Other Systems

- **HONEYBEE: Efficient Role-based Access Control for Vector Databases via Dynamic Partitioning**<br>Hongbin Zhong, Matthew Lentz, Nina Narodytska, Adriana Szekeres, Kexin Rong [[paper]](https://doi.org/10.1145/3786625) [[arXiv]](https://arxiv.org/abs/2505.01538) [[code]](https://github.com/rjzhb/VectorSearch-RBAC) `privacy` `access-control`
- **Integrating Vector Databases across Embedding Models**<br>Beining Yang, Yang Cao, Yang Ren [[paper]](https://doi.org/10.1145/3769803) `embedding-models`

### Benchmarks

- **Attribute Filtering in Approximate Nearest Neighbor Search: An In-depth Experimental Study**<br>Mocheng Li, Xiao Yan, Baotong Lu, Yue Zhang, James Cheng, Chenhao Ma [[paper]](https://doi.org/10.1145/3769763) [[arXiv]](https://arxiv.org/abs/2508.16263) [[code]](https://github.com/lmccccc/FANNBench) `filtered`
- **CANDOR-Bench: Benchmarking In-Memory Continuous ANNS under Dynamic Open-World Streams [Experiments & Analysis]**<br>Mingqi Wang, Junyao Dong, Zhuoyan Wu, Jun Liu, Ruicheng Zhang, Jianjun Zhao, et al. [[paper]](https://doi.org/10.1145/3786630) [[code]](https://github.com/DataSysResearch/CANDOR-Bench) `dynamic`
- **Reveal Hidden Pitfalls and Navigate Next Generation of Vector Similarity Search from Task-Centric Views: [Experiments & Analysis]**<br>Tingyang Chen, Cong Fu, Jiahua Wu, Haotian Wu, Hua Fan, Xiangyu Ke, et al. [[paper]](https://doi.org/10.1145/3786690) [[arXiv]](https://arxiv.org/abs/2512.12980) [[code]](https://github.com/ZJU-DAILY/Iceberg)
- **VecBench: A Controllable Benchmark for Filtered Vector Search: [Experiments & Analysis]**<br>Xiang Zhang, Chao Zhang, Ju Fan, Guoliang Li, Xiaoyong Du [[paper]](https://doi.org/10.1145/3802125) [[code]](https://github.com/ruc-datalab/VecBench) `filtered`

### Workload Characterization

- **An In-Depth Study of Filter-Agnostic Vector Search on a PostgreSQL Database System: [Experiments & Analysis]**<br>Duo Lu, Helena Caminal, Manos Chatzakis, Yannis Papakonstantinou, Yannis Chronis, Vaibhav Jain, et al. [[paper]](https://doi.org/10.1145/3802011) [[arXiv]](https://arxiv.org/abs/2603.23710) [[code]](https://github.com/google-systems-research/fvs) `filtered` `postgres`
- **Building Stateless Serverless Vector DBs via Block-based Data Partitioning**<br>Daniel Barcelona Pons, Raúl Gracia Tinedo, Albert Cañadilla-Domingo, Xavier Roca-Canals, Pedro García López [[paper]](https://doi.org/10.1145/3769769) [[code]](https://github.com/neardata-eu/serverless-vdb) `serverless`
- **Through the Lens of Hubness: A Revisit on Graph-Based Approximate Nearest Neighbor Search: [Experiments & Analysis]**<br>Xiaoliang Xu, Haonan Dai, Can Li, Mengzhao Wang, Qiang Yue [[paper]](https://doi.org/10.1145/3802120) [[code]](https://github.com/H40NaN/GraphANNS-Hubness) `graph`

## SIGMOD 2025

### ANNS Indexing Algorithms

- **Fast Approximate Similarity Join in Vector Databases**<br>Jiadong Xie, Jeffrey Xu Yu, Yingfan Liu [[paper]](https://doi.org/10.1145/3725403) `join`
- **MIRAGE-ANNS: Mixed Approach Graph-based Indexing for Approximate Nearest Neighbor Search**<br>Sairaj Voruganti, M. Tamer Özsu [[paper]](https://doi.org/10.1145/3725325) `graph`
- **Practical and Asymptotically Optimal Quantization of High-Dimensional Vectors in Euclidean Space for Approximate Nearest Neighbor Search**<br>Jianyang Gao, Yutong Gou, Yuexuan Xu, Yongyi Yang, Cheng Long, Raymond Chi-Wing Wong [[paper]](https://doi.org/10.1145/3725413) [[arXiv]](https://arxiv.org/abs/2409.09913) [[code]](https://github.com/VectorDB-NTU/Extended-RaBitQ) `quantization`
- **Subspace Collision: An Efficient and Accurate Framework for High-dimensional Approximate Nearest Neighbor Search**<br>Jiuqi Wei, Xiaodong Lee, Zhenyu Liao, Themis Palpanas, Botao Peng [[paper]](https://doi.org/10.1145/3709729) [[arXiv]](https://arxiv.org/abs/2411.14754) [[code]](https://github.com/WeiJiuQi/SuCo)
- **SymphonyQG: Towards Symphonious Integration of Quantization and Graph for Approximate Nearest Neighbor Search**<br>Yutong Gou, Jianyang Gao, Yuexuan Xu, Cheng Long [[paper]](https://doi.org/10.1145/3709730) [[arXiv]](https://arxiv.org/abs/2411.12229) [[code]](https://github.com/gouyt13/SymphonyQG) `graph` `quantization`

### Filtered ANNS Algorithms

- **DIGRA: A Dynamic Graph Indexing for Approximate Nearest Neighbor Search with Range Filter**<br>Mengxu Jiang, Zhi Yang, Fangyuan Zhang, Guanhao Hou, Jieming Shi, Wenchao Zhou, et al. [[paper]](https://doi.org/10.1145/3725399) [[code]](https://github.com/CUHK-DBGroup/DIGRA) `dynamic`
- **Efficient Dynamic Indexing for Range Filtered Approximate Nearest Neighbor Search**<br>Fangyuan Zhang, Mengxu Jiang, Guanhao Hou, Jieming Shi, Hua Fan, Wenchao Zhou, et al. [[paper]](https://doi.org/10.1145/3725401) [[code]](https://github.com/CUHK-DBGroup/RangePQ) `dynamic`
- **iRangeGraph: Improvising Range-dedicated Graphs for Range-filtering Nearest Neighbor Search**<br>Yuexuan Xu, Jianyang Gao, Yutong Gou, Cheng Long, Christian S. Jensen [[paper]](https://doi.org/10.1145/3698814) [[arXiv]](https://arxiv.org/abs/2409.02571) [[code]](https://github.com/YuexuanXu7/iRangeGraph)
- **Navigating Labels and Vectors: A Unified Approach to Filtered Approximate Nearest Neighbor Search**<br>Yuzheng Cai, Jiayang Shi, Yizhuo Chen, Weiguo Zheng [[paper]](https://doi.org/10.1145/3698822) [[code]](https://github.com/YZ-Cai/Unified-Navigating-Graph)
- **RWalks: Random Walks as Attribute Diffusers for Filtered Vector Search**<br>Anas Ait Aomar, Karima Echihabi, Marco Arnaboldi, Ioannis Alagiannis, Damien Hilloulin, Manal Cherkaoui [[paper]](https://doi.org/10.1145/3725349) [[code]](https://github.com/AnasAito/rwalks-reproduce-v2)

### Hybrid Search Algorithms

- **DEG: Efficient Hybrid Vector Search Using the Dynamic Edge Navigation Graph**<br>Ziqi Yin, Jianyang Gao, Pasquale Balsebre, Gao Cong, Cheng Long [[paper]](https://doi.org/10.1145/3709679) [[arXiv]](https://arxiv.org/abs/2502.07343) [[code]](https://github.com/Heisenberg-Yin/DEG) `hybrid` `graph`

### Vector Databases & Other Systems

- **Accelerating Graph Indexing for ANNS on Modern CPUs**<br>Mengzhao Wang, Haotian Wu, Xiangyu Ke, Yunjun Gao, Yifan Zhu, Wenchao Zhou [[paper]](https://doi.org/10.1145/3725260) [[arXiv]](https://arxiv.org/abs/2502.18113) [[code]](https://github.com/ZJU-DAILY/HNSW-Flash) `graph` `cpu`
- **PDX: A Data Layout for Vector Similarity Search**<br>Leonardo Kuffó, Elena Krippner, Peter Boncz [[paper]](https://doi.org/10.1145/3725333) [[arXiv]](https://arxiv.org/abs/2503.04422) [[code]](https://github.com/cwida/PDX) `layout`
- **PQCache: Product Quantization-based KVCache for Long Context LLM Inference**<br>Hailin Zhang, Xiaodong Ji, Yilin Chen, Fangcheng Fu, Xupeng Miao, Xiaonan Nie, et al. [[paper]](https://doi.org/10.1145/3725338) [[arXiv]](https://arxiv.org/abs/2407.12820) [[code]](https://github.com/HugoZHL/PQCache) `kvcache` `quantization`
- **Tribase: A Vector Data Query Engine for Reliable and Lossless Pruning Compression using Triangle Inequalities**<br>Qian Xu, Juan Yang, Feng Zhang, Junda Pan, Kang Chen, Youren Shen, et al. [[paper]](https://doi.org/10.1145/3709743) [[code]](https://github.com/xuqianmamba/Tribase)

### Benchmarks

- **Graph-Based Vector Search: An Experimental Evaluation of the State-of-the-Art**<br>Ilias Azizi, Karima Echihabi, Themis Palpanas [[paper]](https://doi.org/10.1145/3709693) [[arXiv]](https://arxiv.org/abs/2502.05575) [[code]](https://github.com/iliasazizi/GVS) `graph`
