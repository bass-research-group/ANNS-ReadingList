# VLDB

ANNS and vector search papers at VLDB, all years. Generated from [`data/papers/`](../../data/papers/); edit those files, not this one.

## VLDB 2027

### Filtered ANNS Algorithms

- **VectorMaton: Efficient Vector Search with Pattern Constraints via an Enhanced Suffix Automaton** *(accepted, to appear)*<br>Haoxuan Xie, Siqiang Luo [[arXiv]](https://arxiv.org/abs/2603.01525) [[code]](https://github.com/ForwardStar/VectorMaton)

### Hybrid Search Algorithms

- **CORAL: Cross-modal Vector Retrieval via Incremental Graph Construction at Scale** *(accepted, to appear)*<br>Shixin Wan, Guoyu Hu, Yifan Wu, et al. [[arXiv]](https://arxiv.org/abs/2610.11230) `graph` `cross-modal` `dynamic`

### Vector Databases & Other Systems

- **Can You Trust the Vectors in Your Vector Database? Black-Hole Attack from Embedding Space Defects** *(accepted, to appear)*<br>Hanxi Li, Jiale Lao, Zhengmao Ye, et al. [[arXiv]](https://arxiv.org/abs/2604.05480) [[code]](https://github.com/hanxi19/Black_Hole_Attack_for_Vector_Database) `security` `hubness`
- **HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search** *(accepted, to appear)*<br>Fahong Zhang, Weijie Jin, Lixu Wang, et al. `privacy` `mpc` `graph`

### Benchmarks

- **DiskVecLab: A Deployment-Realistic Evaluation Framework for Disk-Based Vector Search** *(accepted, to appear)*<br>Yuxiang Wang, Yongxin Tong, Shuyuan Li, et al. [[code]](https://github.com/alibaba/DiskVecLab) `disk`

## VLDB 2026

### ANNS Indexing Algorithms

- **A Topology-Aware Localized Update Strategy for Graph-Based ANN Index**<br>Song Yu, Shengyuan Lin, Shufeng Gong, Yongqing Xie, Ruicheng Liu, Yijie Zhou, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p495-yu.pdf) [[code]](https://github.com/iDC-NEU/Greator) `graph` `dynamic`
- **CONDA: A Connectivity-Aware Dynamic Index for Approximate Nearest Neighbor Search over Evolving Data**<br>Darae Lee, Min-Soo Kim [[paper]](https://www.vldb.org/pvldb/vol19/p3357-lee.pdf) [[code]](https://github.com/darae-lee/CONDA) `dynamic` `graph`
- **HEXA: A Disjoint-Subgraph-Based Indexing Framework for Approximate Nearest Neighbor Search at Billion Scale**<br>Yifei Xu, Yanyan Shen, Youmin Chen, Linpeng Huang [[paper]](https://www.vldb.org/pvldb/vol19/p2922-shen.pdf) `graph` `billion-scale`
- **JHQ: Johnson-Lindenstrauss Enhanced Hierarchical Quantization for High-Dimensional Approximate Nearest Neighbor Search**<br>Jiabao Han, Mengxuan Zhang, Goce Trajcevski [[paper]](https://www.vldb.org/pvldb/vol19/p1530-han.pdf) [[code]](https://github.com/ANU-DB-Mengxuan-Group/VLDB26-JHQ) `quantization`
- **Quantization Meets Projection: A Happy Marriage for Approximate k-Nearest Neighbor Search**<br>Mingyu Yang, Liuchang Jing, Wentao Li, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p1240-yang.pdf) [[code]](https://github.com/mingyu-hkustgz/RESQ) `quantization`
- **Sparse Neighborhood Graph-Based Approximate Nearest Neighbor Search Revisited: Theoretical Analysis and Optimization**<br>Xinran Ma, Zhaoqi Zhou, Chuan Zhou, Zaijiu Shang, Guoliang Li, Zhiming Ma [[paper]](https://www.vldb.org/pvldb/vol19/p2817-zhou.pdf) [[code]](https://github.com/maxila320/OPT-SNG) `graph` `theory`

### ANNS Search Optimization & Tuning

- **ANNiE: A Learned Query Cost Estimator for Graph-Based Approximate Nearest Neighbor Search**<br>Zeyu Wang, Manos Chatzakis, Qitong Wang, Themis Palpanas, Peng Wang, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p3820-wang.pdf) [[code]](https://github.com/CaucherWang/ANNiE) `graph` `cost-model`
- **BBC: Improving Large-𝑘 Approximate Nearest Neighbor Search with a Bucket-based Result Collector**<br>Ziqi Yin, Gao Cong, Kai Zeng, Jinwei Zhu, Bin Cui [[paper]](https://www.vldb.org/pvldb/vol19/p3468-yin.pdf) [[code]](https://github.com/Heisenberg-Yin/BBC) `large-k`
- **ConANN: Conformal Approximate Nearest Neighbor Search**<br>Sonia Horchidan, Fabian Zeiher, Henrik Boström, Paris Carbone [[paper]](https://www.vldb.org/pvldb/vol19/p29-horchidan.pdf) [[code]](https://github.com/soniahorchidan/conann)
- **QBAT: Model-based Query Budget Autotuner for Clustering-based Approximate Nearest Neighbor Search**<br>Jonghyun Bae, Tae Jun Ham, Alan Li, Supawit Chockchowwat, Yannis Papakonstantinou [[paper]](https://www.vldb.org/pvldb/vol19/p3091-chockchowwat.pdf) `ivf` `tuning`

### Filtered ANNS Algorithms

- **CGIF: Combining Proximity Graphs and Inverted Files for Efficient Filtered Vector Search over Arbitrary Predicates**<br>Jiarui Luo, Chaoji Zuo, Dong Deng [[paper]](https://www.vldb.org/pvldb/vol19/p3663-luo.pdf) [[code]](https://github.com/rutgers-db/CGIF)
- **Elastic Index Selection for Label-Hybrid AKNN Search**<br>Mingyu Yang, Wenxuan Xia, Wentao Li, Raymond Chi-Wing Wong, Wei Wang [[paper]](https://www.vldb.org/pvldb/vol19/p617-yang.pdf) [[code]](https://github.com/mingyu-hkustgz/LabelANN)
- **GAS: A Lightweight Framework for Filtered Search over Wide-table Vectors**<br>Ziyuan He, Yuxiang Wang, Yu Sun, Zijie Ma, Hui Li, Qian Tao, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p3133-tong.pdf)
- **Harmonizing Efficiency and Accuracy in Filtered Vector Search**<br>Zixiang Zhou, Xuhao Chen [[paper]](https://www.vldb.org/pvldb/vol19/p2059-chen.pdf) [[code]](https://github.com/zhouzixiang2004/BigFANN)<br><sub>The BigFANN paper.</sub>
- **RNSG: A Range-Aware Graph Index for Efficient Range-Filtered Approximate Nearest Neighbor Search**<br>Zhiqiu Zou, Ziqi Yin, Rong-Hua Li, Hongchao Qin, Qiangqiang Dai, Guoren Wang [[paper]](https://www.vldb.org/pvldb/vol19/p2839-zou.pdf) [[code]](https://github.com/fallleaves01/R-NSG)

### GPU-Accelerated ANNS Systems

- **GPU-Accelerated ANNS: Quantized for Speed, Built for Change**<br>Hunter McCoy, Zikun Wang, Prashant Pandey [[paper]](https://www.vldb.org/pvldb/vol19/p3413-pandey.pdf) [[code]](https://github.com/zikunw/jasper) `quantization` `dynamic`
- **GPU-Native Approximate Nearest Neighbor Search with IVF-RaBitQ: Fast Index Build and Search**<br>Jifan Shi, Jianyang Gao, James Xia, Tamas B. Fehér, Cheng Long [[paper]](https://www.vldb.org/pvldb/vol19/p3454-shi.pdf) [[code]](https://github.com/VectorDB-NTU/cuvs_rabitq) `quantization`
- **SVFusion: A CPU-GPU Co-Processing Architecture for Large-Scale Real-Time Vector Search**<br>Yuchen Peng, Dingyu Yang, Zhongle Xie, Ji Sun, Lidan Shou, Ke Chen, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1074-yang.pdf) [[code]](https://github.com/zjuDBxAI/svfusion) `dynamic`

### Distributed ANNS Systems

- **FedBridge: A Federated Query Engine over Embedding-Heterogeneous Vector Databases**<br>Yuxiang Wang, Ruixi Hu, Ziyuan He, Zhilin Liang, Xinyu Zhao, Yongxin Tong [[paper]](https://www.vldb.org/pvldb/vol19/p4498-tong.pdf) [[code]](https://github.com/Roy-buaa/FedBridge) `federated`
- **RED-ANNS: A RDMA-Enabled Distributed Framework for Graph-Based Approximate Nearest Neighbor Search**<br>Yue Chen, Kai Zhang, Sipeng Chen, Shihai Xiao, Xiaomin Zou, Ren Ren, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p399-chen.pdf) [[code]](https://github.com/cheenyuee/RED-ANNS) `rdma` `graph`

### Vector Databases & Other Systems

- **Aker: Density-Aware Approximate Caching for Vector Search**<br>Sukjoon Oh, Minki Kang, Dohyun Kim, Baotong Lu, Jing Liu, Qianxi Zhang, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p2727-oh.pdf) [[code]](https://github.com/sjoon-oh/Aker) `caching`
- **Nova: A Multi-Purpose Vector Engine for Low-Latency, Multi-Tenant, and Cross-Table Hybrid Retrieval**<br>Dechuang Chen, Bing Chen, Jianwei Lu, Zhiwei Wu, Zeyu Yang, Qiang Gu, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p4453-zhou.pdf) `hybrid` `vector-db`
- **RetroInfer: A Vector Storage Engine for Scalable Long-Context LLM Inference**<br>Yaoqi Chen, Jinkai Zhang, Baotong Lu, Qianxi Zhang, Chengruidong Zhang, Jing Liu, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1016-lu.pdf) [[code]](https://github.com/microsoft/RetrievalAttention) `kvcache`
- **SQL-Native Vector Search at Billion Scale in Presto**<br>Zhichen Xu, Ge Gao, Ke Wang, Aakash Deep, Junjie Qi, Jort Gemmeke, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p4182-xu.pdf) `vector-db`
- **TEngineDB-V: An OLAP-Native Vector Search System for Large-𝑘 Workloads at Tencent**<br>Xufei Wu, Pengcheng Zhang, Yitong Song, Xiaobo Zhang, Anqi Liang, Kai Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p3955-zhou.pdf) `vector-db`
- **V3DB: Audit-on-Demand Zero-Knowledge Proofs for Verifiable Vector Search over Committed Snapshots**<br>Zipeng Qiu, Wenjie Qu, Jiaheng Zhang, Binhang Yuan [[paper]](https://www.vldb.org/pvldb/vol19/p2604-qiu.pdf) [[code]](https://github.com/TabibitoQZP/zk-IVF-PQ) `zkp` `verifiable`

### Benchmarks

- **An Experimental Evaluation of Hybrid Querying on Vectors**<br>Jiaxu Zhu, Jiayu Yuan, Kaiwen Yang, Xiaobao Chen, Shihuan Yu, Hongchang Lv, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p183-zheng.pdf) [[code]](https://github.com/zhujx001/Hybrid-ANNS-Experiment) `filtered`
- **Balancing the Blend: An Experimental Analysis of Trade-offs in Hybrid Search**<br>Mengzhao Wang, Boyu Tan, Yunjun Gao, Hai Jin, Yingfeng Zhang, Xiangyu Ke, et al. [[paper]](https://www.vldb.org/pvldb/vol19/p1715-gao.pdf) [[code]](https://github.com/infiniflow/infinity) `hybrid`
- **Disk-Resident Graph ANN Search: An Experimental Evaluation** *(accepted, to appear)*<br>Xiaoyu Chen, Jinxiu Qu, Yitong Song, et al. [[arXiv]](https://arxiv.org/abs/2603.01779) [[code]](https://github.com/hkbudb/disk-vss-survey) `disk` `graph`<br><sub>PVLDB 2026 per the code README; not yet in DBLP.</sub>
- **Revisiting Filtered ANN Benchmarks: A Hardness-Controlled Benchmark Generator for Realistic Evaluation**<br>Mintaek Lim, Dogeun Kim, Minwoo Kim, Jaeyoung Do [[paper]](https://www.vldb.org/pvldb/vol19/p2763-lim.pdf) [[code]](https://github.com/AIDAS-Lab/FANN_Benchmark) `filtered`
- **Towards Robustness: A Critique of Current Vector Database Assessments** *(accepted, to appear)*<br>Zikai Wang, Qianxi Zhang, Baotong Lu, et al. [[arXiv]](https://arxiv.org/abs/2507.00379) [[code]](https://github.com/khaiwang/ANN-Robustness-Submission) `robustness`<br><sub>VLDB 2026 per the artifact README; not yet in DBLP.</sub>

### Workload Characterization

- **I/O Optimizations in Graph-Based Disk-Resident Approximate Nearest Neighbor Search: A Design Space Exploration**<br>Liang Li, Shufeng Gong, Yanan Yang, Yiduo Wang, Jie Wu [[paper]](https://www.vldb.org/pvldb/vol19/p1484-li.pdf) [[code]](https://github.com/LeonLee666/IObench4DiskANN) `disk`

### Surveys

- **Advances of Query Processing in Vector Databases**<br>Jiadong Xie, Yingfan Liu, Jeffrey Xu Yu [[paper]](https://www.vldb.org/pvldb/vol19/p4893-xie.pdf)

## VLDB 2025

### ANNS Indexing Algorithms

- **Accelerating Approximate Nearest Neighbor Search in Hierarchical Graphs: Efficient Level Navigation with Shortcuts**<br>Zengyang Gong, Yuxiang Zeng, Lei Chen [[paper]](https://www.vldb.org/pvldb/vol18/p3518-chen.pdf) `graph`
- **Cracking Vector Search Indexes**<br>Vasilis Mageirakos, Bowen Wu, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p3951-mageirakos.pdf) [[code]](https://github.com/mageirakos/crack-ivf-vldb) `adaptive`
- **GTI: Graph-based Tree Index with Logarithm Updates for Nearest Neighbor Search in High-Dimensional Spaces**<br>Ruiyao Ma, Yifan Zhu, Baihua Zheng, Lu Chen, Congcong Ge, Yunjun Gao [[paper]](https://www.vldb.org/pvldb/vol18/p986-gao.pdf) [[code]](https://github.com/ZJU-DAILY/GTI-Graph-based-Tree-Index) `dynamic`
- **Maximum Inner Product is Query-Scaled Nearest Neighbor**<br>Tingyang Chen, Cong Fu, Kun Wang, Xiangyu Ke, Yunjun Gao, Wenchao Zhou, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p1770-ke.pdf) [[code]](https://github.com/ZJU-DAILY/PSP) `mips`
- **Not Small Enough? SegPQ: A Learned Approach to Compress Product Quantization Codebooks**<br>Qiyu Liu, Yanlin Qi, Siyuan Han, Jingshu Peng, Jin Li, Lei Chen [[paper]](https://www.vldb.org/pvldb/vol18/p3730-liu.pdf) [[code]](https://github.com/qyliu-hkust/segpq) `quantization`
- **Revisiting the Index Construction of Proximity Graph-Based Approximate Nearest Neighbor Search**<br>Shuo Yang, Jiadong Xie, Yingfan Liu, Jeffrey Xu Yu, Xiyue Gao, Qianru Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p1825-liu.pdf) [[code]](https://github.com/xdyangsh/FastKCNA) `graph`
- **Wolverine: Highly Efficient Monotonic Search Path Repair for Graph-based ANN Index Updates**<br>Dawei Liu, Bolong Zheng, Ziyang Yue, Fuhao Ruan, Xiaofang Zhou, Christian S. Jensen [[paper]](https://www.vldb.org/pvldb/vol18/p2268-zheng.pdf) [[code]](https://github.com/LDW2020/Wolverine) `graph` `dynamic`

### ANNS Search Optimization & Tuning

- **Cardinality Estimation for Similarity Search on High-Dimensional Data Objects: The Impact of Reference Objects**<br>Hai Lan, Shixun Huang, Zhifeng Bao, Renata Borovica-Gajic [[paper]](https://www.vldb.org/pvldb/vol18/p544-bao.pdf) [[code]](https://github.com/rmitbggroup/CE4HD)
- **Efficient Data-aware Distance Comparison Operations for High-Dimensional Approximate Nearest Neighbor Search**<br>Liwei Deng, Penghao Chen, Ximu Zeng, Tianfu Wang, Yan Zhao, Kai Zheng [[paper]](https://www.vldb.org/pvldb/vol18/p812-zheng.pdf) [[code]](https://github.com/Ur-Eine/DADE)

### Filtered ANNS Algorithms

- **Dynamic Range-Filtering Approximate Nearest Neighbor Search**<br>Zhencan Peng, Miao Qiao, Wenchao Zhou, Feifei Li, Dong Deng [[paper]](https://www.vldb.org/pvldb/vol18/p3256-deng.pdf) [[code]](https://github.com/rutgers-db/DynamicSegmentGraph) `dynamic`
- **SIEVE: Effective Filtered Vector Search with Collection of Indexes**<br>Zhaoheng Li, Silu Huang, Wei Ding, Yongjoo Park, Jianjun Chen [[paper]](https://www.vldb.org/pvldb/vol18/p4723-li.pdf) [[code]](https://github.com/BillyZhaohengLi/SIEVE-vldb25)
- **UNIFY: Unified Index for Range Filtered Approximate Nearest Neighbors Search**<br>Anqi Liang, Pengcheng Zhang, Bin Yao, Zhongpu Chen, Yitong Song, Guangxu Cheng [[paper]](https://www.vldb.org/pvldb/vol18/p1118-yao.pdf) [[code]](https://github.com/sjtu-dbgroup/UNIFY)

### Out-of-Core ANNS Systems

- **Select Edges Wisely: Monotonic Path Aware Graph Layout Optimization for Disk-based ANN Search**<br>Ziyang Yue, Bolong Zheng, Ling Xu, Kanru Xu, Shuhao Zhang, Yajuan Du, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p4337-zheng.pdf) [[code]](https://github.com/CodenameYZY/MARGO) `disk` `graph`
- **Turbocharging Vector Databases using Modern SSDs**<br>Joobo Shim, Jaewon Oh, Hongchan Roh, Jaeyoung Do, Sang-Won Lee [[paper]](https://www.vldb.org/pvldb/vol18/p4710-do.pdf) [[code]](https://github.com/FlashSQL/io-optimized-pgvector) `disk`

### Distributed ANNS Systems

- **HAKES: Scalable Vector Database for Embedding Search Service**<br>Guoyu Hu, Shaofeng Cai, Tien Tuan Anh Dinh, Zhongle Xie, Cong Yue, Gang Chen, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p3049-ooi.pdf) [[code]](https://github.com/nusdbsystem/HAKES)
- **Unleashing Graph Partitioning for Large-Scale Nearest Neighbor Search**<br>Lars Gottesbüren, Laxman Dhulipala, Rajesh Jayaram, Jakub Lacki [[paper]](https://www.vldb.org/pvldb/vol18/p1649-gottesbueren.pdf) [[code]](https://github.com/larsgottesbueren/gp-ann) `partition`
- **VStream: A Distributed Streaming Vector Search System**<br>Shenghao Gong, Haobo Sun, Ziquan Fang, Liu Liu, Lu Chen, Yunjun Gao [[paper]](https://www.vldb.org/pvldb/vol18/p1593-gao.pdf) [[code]](https://github.com/ZJU-DAILY/VStream) `dynamic`

### Vector Databases & Other Systems

- **Cost-Effective, Low Latency Vector Search with Azure Cosmos DB**<br>Nitish Upreti, Harsha Vardhan Simhadri, Hari Sudan Sundar, Krishnan Sundaram, Samer Boshra, Balachandar Perumalswamy, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p5166-upreti.pdf) `vector-db` `cloud`
- **FedVSE: A Privacy-Preserving and Efficient Vector Search Engine for Federated Databases**<br>Zeheng Fan, Yuxiang Zeng, Zhuanglin Zheng, Yongxin Tong [[paper]](https://www.vldb.org/pvldb/vol18/p5371-tong.pdf) `privacy` `federated`
- **GaussDB-Vector: A Large-Scale Persistent Real-Time Vector Database for LLM Applications**<br>Guoliang Li, Ji Sun, James Pan, Jiang Wang, Yongqing Xie, Ruicheng Liu, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p4951-sun.pdf) `vector-db`
- **NaviX: A Native Vector Index Design for Graph DBMSs With Robust Predicate-Agnostic Search Performance**<br>Gaurav Sehgal, Semih Salihoglu [[paper]](https://www.vldb.org/pvldb/vol18/p4438-sehgal.pdf) [[code]](https://github.com/gaurav8297/kuzu) `filtered` `graph-dbms`
- **VSAG: An Optimized Search Framework for Graph-based Approximate Nearest Neighbor Search**<br>Xiaoyao Zhong, Haotian Li, Jiabao Jin, Mingyu Yang, Deming Chu, Xiangyu Wang, et al. [[paper]](https://www.vldb.org/pvldb/vol18/p5017-cheng.pdf) [[code]](https://github.com/antgroup/vsag) `graph`

### FPGA & In-storage Acceleration

- **Chameleon: a Heterogeneous and Disaggregated Accelerator System for Retrieval-Augmented Language Models**<br>Wenqi Jiang, Marco Zeller, Roger Waleffe, Torsten Hoefler, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p42-jiang.pdf) [[code]](https://github.com/WenqiJiang/Chameleon) `rag` `disaggregated`
- **Fast Graph Vector Search via Hardware Acceleration and Delayed-Synchronization Traversal**<br>Wenqi Jiang, Hang Hu, Torsten Hoefler, Gustavo Alonso [[paper]](https://www.vldb.org/pvldb/vol18/p3797-jiang.pdf) [[code]](https://github.com/fpgasystems/Falcon-accelerate-graph-vector-search) `fpga` `graph`

### Benchmarks

- **BigVectorBench: Heterogeneous Data Embedding and Compound Queries are Essential in Evaluating Vector Databases**<br>Guoxin Kang, Zhongxin Ge, Jingpei Hu, Xueya Zhang, Lei Wang, Jianfeng Zhan [[paper]](https://www.vldb.org/pvldb/vol18/p1536-zhan.pdf) [[code]](https://github.com/BenchCouncil/BigVectorBench)

### Surveys

- **Filtered Vector Search: State-of-the-art and Research Challenges**<br>Helena Caminal, Yannis Chronis, Yannis Papakonstantinou, Fatma Özcan, Anastasia Ailamaki [[paper]](https://www.vldb.org/pvldb/vol18/p5488-caminal.pdf) `filtered`
