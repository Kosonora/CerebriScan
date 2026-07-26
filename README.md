# CerebraScan: Intelligent Stroke Identification and Segmentation System Based on Non-Contrast CT
# CerebraScan：基于平扫CT的卒中智能识别与分割系统

---

## 1. Background
## 一、背景

### 1.1 Epidemiology of Stroke
### 1.1 卒中的流行病学

Stroke is one of the leading causes of disability and death worldwide. According to the Global Burden of Disease study published in *The Lancet Neurology*, stroke has become the second leading cause of death globally, with over 12 million new cases annually. In China, stroke is the leading cause of death and adult disability, with approximately 2.4 million new cases each year, and the incidence rate continues to rise. Stroke not only severely threatens patients" health but also imposes a heavy economic burden on society and families.

脑卒中（Stroke）是全球范围内致残和致死的首要病因之一。根据《Lancet Neurology》全球疾病负担研究数据，卒中已成为全球第二大死亡原因，每年新发病例超过1200万例。在中国，卒中是第一位死亡原因和成人致残的首要病因，我国每年新发卒中患者约240万例，且发病率呈持续上升趋势。卒中不仅严重威胁患者生命健康，还给社会和家庭带来沉重的经济负担。

### 1.2 Etiology
### 1.2 病因

#### Ischemic Stroke
#### 缺血性卒中

Ischemic stroke accounts for approximately 70%–80% of all strokes. Its main etiologies include:

- **Large Artery Atherosclerosis**: Atherosclerotic plaque formation in the internal carotid artery, middle cerebral artery, and other major intracranial and extracranial arteries, leading to stenosis or occlusion. This is the most common cause of ischemic stroke.
- **Cardioembolism**: Atrial fibrillation is the most common cause, along with valvular heart disease, myocardial infarction with mural thrombus, and infective endocarditis.
- **Small Vessel Occlusion**: Long-standing hypertension and diabetes cause hyalinosis of perforating arteries, leading to lacunar infarcts.
- **Other Determined Etiologies**: Including arterial dissection, vasculitis, Moyamoya disease, and hematologic disorders.
- **Undetermined Etiology**: Cases where the cause remains unidentified after thorough investigation.

缺血性卒中约占所有卒中的70%~80%，其病因主要包括：
- **大动脉粥样硬化（Large Artery Atherosclerosis）**：颈内动脉、大脑中动脉等颅内外大动脉的粥样硬化斑块形成，导致血管狭窄或闭塞，是缺血性卒中最常见的病因。
- **心源性栓塞（Cardioembolism）**：以心房颤动最为常见，此外还包括瓣膜性心脏病、心肌梗死伴附壁血栓、感染性心内膜炎等。
- **小血管病变（Small Vessel Occlusion）**：长期高血压、糖尿病导致穿支动脉玻璃样变性，引起腔隙性脑梗死。
- **其他明确病因**：包括动脉夹层、血管炎、烟雾病、血液系统疾病等。
- **不明原因型**：经充分检查仍无法明确病因者。

#### Hemorrhagic Stroke
#### 出血性卒中

Hemorrhagic stroke accounts for approximately 20%–30% of all strokes. Its main etiologies include:

- **Hypertensive Intracerebral Hemorrhage**: Long-standing hypertension causes fibrinoid necrosis of small artery walls or microaneurysm formation. This is the most common cause of spontaneous intracerebral hemorrhage.
- **Cerebral Amyloid Angiopathy (CAA)**: Amyloid protein deposits in the walls of cortical small vessels, commonly seen in the elderly, often causing lobar hemorrhage.
- **Arteriovenous Malformation (AVM)**: Congenital vascular developmental anomaly.
- **Ruptured Intracranial Aneurysm**: Commonly presents as subarachnoid hemorrhage.
- **Others**: Cerebral venous sinus thrombosis, coagulopathy, vasculitis, tumor-related hemorrhage, etc.

出血性卒中约占20%~30%，其病因主要包括：
- **高血压性脑出血**：长期高血压导致小动脉壁纤维素样坏死或微动脉瘤形成，是自发性脑出血的最常见原因。
- **脑淀粉样血管病（CAA）**：淀粉样蛋白沉积于脑皮层小血管壁，多见于老年人，常引起脑叶出血。
- **动静脉畸形（AVM）**：先天性血管发育异常。
- **颅内动脉瘤破裂**：常见于蛛网膜下腔出血。
- **其他**：颅内静脉窦血栓、凝血功能障碍、血管炎、肿瘤卒中等。

### 1.3 Pathogenesis
### 1.3 发病机制

#### Ischemic Stroke
#### 缺血性卒中

The core mechanism of ischemic stroke is a sharp decline in cerebral blood flow leading to neuronal energy metabolism failure. After thrombus formation or embolic occlusion of cerebral vessels, a cascade of events occurs in the ischemic region: energy depletion → glutamate excitotoxicity → calcium overload → free radical generation → oxidative stress → mitochondrial dysfunction → inflammatory cascade → apoptosis and necrosis. The concept of the **ischemic penumbra** is the pathophysiological basis of acute ischemic stroke treatment — before penumbral neurons undergo irreversible damage, early restoration of blood perfusion can salvage the dying brain tissue.

缺血性卒中的核心机制为脑血流量急剧下降导致神经元能量代谢衰竭。血栓形成或栓塞堵塞脑血管后，脑组织缺血区出现一系列级联反应：能量耗竭→谷氨酸兴奋性毒性→钙离子超载→自由基生成→氧化应激→线粒体功能障碍→炎症级联反应→细胞凋亡与坏死。缺血半暗带（Ischemic Penumbra）的概念是急性缺血性卒中治疗的病理生理学基础——在半暗带神经元尚未发生不可逆损伤之前，尽早恢复血流灌注可挽救濒死脑组织。

#### Hemorrhagic Stroke
#### 出血性卒中

After intracranial vessel rupture, the hematoma directly exerts mass effect and mechanical destruction on surrounding brain tissue. Meanwhile, hematoma components (such as thrombin and hemoglobin degradation products) trigger secondary brain edema, inflammatory responses, and neuronal toxicity. Hematoma expansion is a key predictor of early neurological deterioration. As the disease progresses, perihematomal edema intensifies, potentially leading to elevated intracranial pressure and even cerebral herniation.

颅内血管破裂后，血肿直接对周围脑组织产生占位效应和机械性破坏，同时血肿成分（如凝血酶、血红蛋白降解产物）诱发继发性脑水肿、炎症反应和神经元毒性。血肿扩大是早期神经功能恶化的关键预测因素。随病程进展，血肿周围脑水肿逐渐加重，严重者可致颅内压升高甚至脑疝。

### 1.4 Common Clinical Classification
### 1.4 临床常见分型

#### Classification of Ischemic Stroke
#### 缺血性卒中的分型

- **TOAST Classification** (the most widely used etiological classification):
  - Large Artery Atherosclerosis (LAA)
  - Cardioembolism (CE)
  - Small Vessel Occlusion (SVO)
  - Stroke of Other Determined Etiology (SOE)
  - Stroke of Undetermined Etiology (SUE)

- **Oxfordshire Classification** (based on anatomical location of infarction):
  - Total Anterior Circulation Infarct (TACI)
  - Partial Anterior Circulation Infarct (PACI)
  - Posterior Circulation Infarct (POCI)
  - Lacunar Infarct (LACI)

- **TOAST分型**（目前国际最常用的病因学分型）：
  - 大动脉粥样硬化型（LAA）
  - 心源性栓塞型（CE）
  - 小血管闭塞型（SVO）
  - 其他明确病因型（SOE）
  - 不明原因型（SUE）

- **牛津shire分型**（基于梗死灶解剖部位）：
  - 全前循环梗死（TACI）
  - 部分前循环梗死（PACI）
  - 后循环梗死（POCI）
  - 腔隙性梗死（LACI）

#### Classification of Hemorrhagic Stroke
#### 出血性卒中的分型

- **By Location**: Basal ganglia hemorrhage (most common), thalamic hemorrhage, lobar hemorrhage, brainstem hemorrhage, cerebellar hemorrhage, intraventricular hemorrhage.
- **By Etiology**: Primary intracerebral hemorrhage (hypertensive, CAA) and secondary intracerebral hemorrhage (AVM, aneurysm, tumor-related hemorrhage, coagulopathy, etc.).

- **按出血部位**：基底节区出血（最常见）、丘脑出血、脑叶出血、脑干出血、小脑出血、脑室出血。
- **按病因分类**：原发性脑出血（高血压性、CAA）与继发性脑出血（AVM、动脉瘤、肿瘤卒中、凝血障碍等）。

---

## 2. Non-Contrast CT in Stroke
## 二、平扫CT在卒中中的应用

### 2.1 First-Line Imaging in Emergency Settings
### 2.1 急诊首选影像学检查

Non-contrast CT (NCCT) is the first-line imaging modality for acute stroke patients, offering the following advantages: rapid acquisition (completed within minutes), high equipment availability (accessible in most primary care hospitals), no absolute contraindications, and low cost. Both the Chinese Guidelines for the Diagnosis and Treatment of Acute Ischemic Stroke (2024 edition) and the AHA/ASA Guidelines recommend that suspected stroke patients should undergo NCCT examination **within 25 minutes** of arrival at the emergency department.

The core value of NCCT lies in its ability to **rapidly rule out intracranial hemorrhage** — a critical prerequisite for determining whether a patient is eligible for thrombolysis or thrombectomy.

平扫CT（Non-contrast CT, NCCT）是急性卒中患者首选的影像学检查手段，具有以下优势：检查速度快、设备普及率高、无绝对禁忌证、费用低廉。中国急性缺血性脑卒中诊治指南（2024版）及美国心脏协会/美国卒中协会（AHA/ASA）指南均推荐：疑似卒中患者应在到达急诊后**25分钟内**完成平扫CT检查。

平扫CT的核心价值在于**快速排除脑出血**——这是决定患者能否接受溶栓或取栓治疗的关键前提。

### 2.2 Detection of Hemorrhagic Stroke
### 2.2 出血性卒中的识别

NCCT has extremely high sensitivity for acute intracerebral hemorrhage and is considered the "gold standard" for diagnosis. Acute hematoma appears as a well-defined hyperdense lesion on CT, allowing rapid assessment of:

- **Hematoma Location and Size**: Critical for determining the cause of bleeding and prognosis.
- **Signs Predictive of Hematoma Expansion**: Recent studies have identified several NCCT signs that effectively predict the risk of hematoma expansion, including:
  - **Blend Sign**: A mixture of hypodense and hyperdense regions within the hematoma
  - **Swirl Sign**: Iso-/hypodense areas within the hematoma
  - **Black Hole Sign**: A relatively hypodense region encapsulated within a hyperdense hematoma
  - **Island Sign**: Scattered small hematoma foci surrounding the main hematoma
- **Subarachnoid Hemorrhage**: Manifested as hyperdensity within the sulci and cisterns.

平扫CT对急性脑出血具有极高的敏感性（接近100%），是诊断脑出血的"金标准"。急性期血肿在CT上表现为边界清楚的高密度影（CT值约50~90 HU），可快速判断：
- **血肿部位与大小**：对判断出血病因和预后有重要价值。
- **血肿扩大预测征象**：近年来研究发现，平扫CT上的一些影像学征象可有效预测血肿扩大风险，包括：
  - **混合征（Blend Sign）**：血肿内部出现低密度区与高密度区混杂
  - **漩涡征（Swirl Sign）**：血肿内出现等/低密度区
  - **黑洞征（Black Hole Sign）**：相对高密度血肿内包裹低密度区域
  - **岛征（Island Sign）**：血肿周围出现散在的小血肿灶
- **蛛网膜下腔出血**：表现为脑沟、脑池内高密度影。

### 2.3 Early Signs of Ischemic Stroke
### 2.3 缺血性卒中的早期征象

Although DWI-MRI is the most sensitive modality for detecting hyperacute ischemia, NCCT can still reveal several valuable early signs in acute ischemic stroke:

- **Hyperdense Middle Cerebral Artery Sign (HMCAS)**: Reflects thrombus within the MCA, with very high specificity for large vessel occlusion.
- **Insular Ribbon Sign**: Loss of gray-white matter differentiation in the insular cortex.
- **Lentiform Nucleus Blurring**: Loss of gray-white matter differentiation in the basal ganglia region.
- **Sulcal Effacement / Parenchymal Hypodensity**: Reflects cytotoxic edema.

The **ASPECTS (Alberta Stroke Program Early CT Score)** is the most widely used semi-quantitative assessment system in clinical practice. It divides the MCA territory into 10 regions (M1–M6, insular cortex, lentiform nucleus, caudate nucleus, and posterior limb of the internal capsule), deducting 1 point for each region involved. ASPECTS ≥ 7 typically indicates that the patient is suitable for endovascular therapy, while ≤ 6 suggests a poor prognosis.

虽然MRI的DWI序列对超早期缺血灶的检出最为敏感，但平扫CT在缺血性卒中急性期仍能发现一些有价值的早期征象：
- **大脑中动脉高密度征（Hyperdense MCA Sign）**：反映MCA内血栓形成，对大血管闭塞的特异性极高。
- **岛带征（Insular Ribbon Sign）**：岛叶皮层灰白质分界消失。
- **豆状核模糊征（Lentiform Nucleus Blurring）**：基底节区灰白质分界消失。
- **皮层脑沟消失/脑实质低密度**：反映细胞毒性水肿。
- **ASPECTS评分**（Alberta Stroke Program Early CT Score）是目前临床应用最广泛的半定量评估系统，将大脑中动脉供血区划分为10个区域，每累及一个区域扣1分。ASPECTS≥7分通常提示患者适合血管内治疗。

### 2.4 Limitations of NCCT
### 2.4 平扫CT的局限性

- Low sensitivity for detecting hyperacute infarcts (<3–6 hours), far inferior to DWI-MRI.
- Particularly difficult to identify posterior circulation infarcts (brainstem, cerebellum), which are prone to missed diagnosis.
- Limited ability to detect microbleeds.
- **The introduction of deep learning technology** offers new possibilities to overcome these limitations. By automatically extracting complex texture features from CT images, AI models can potentially identify subtle infarct signs on NCCT that are imperceptible to the naked eye, thereby improving the accuracy of early diagnosis.

- 超早期（<3~6小时）梗死灶检出率低，敏感性远低于DWI-MRI。
- 后循环梗死（脑干、小脑）的识别尤为困难，易漏诊。
- 对微小出血灶的识别能力有限。
- **深度学习技术的引入**为克服上述局限性提供了新的可能：通过自动提取CT图像的复杂纹理特征，AI模型有望在平扫CT上识别出肉眼难以发现的细微梗死征象，从而提高早期诊断的准确性。

---

## 3. Project Introduction: CerebraScan
## 三、项目简介：CerebraScan

### 3.1 Project Overview
### 3.1 项目概述

CerebraScan is a deep learning system for intelligent stroke identification and segmentation based on non-contrast CT. It aims to assist clinicians in rapidly and accurately performing three-class classification (normal / ischemic stroke / hemorrhagic stroke) and pixel-level lesion segmentation in emergency settings, thereby providing objective imaging evidence for early diagnosis and individualized treatment decisions.

CerebraScan是一个基于平扫CT的卒中智能识别与分割深度学习系统，旨在利用人工智能技术辅助临床医生在急诊场景下快速、准确地对卒中进行三分类（正常/缺血性卒中/出血性卒中）以及对病灶进行像素级精确分割，从而为卒中患者的早期诊断和个体化治疗决策提供客观的影像学依据。

### 3.2 Dataset
### 3.2 数据集

The project has constructed a large-scale non-contrast CT stroke imaging dataset containing **6,650** CT slice images (512×512 pixels, PNG format) from real clinical scenarios, covering three categories:

| Category | Sample Size | Label | Annotation |
|----------|------------|-------|------------|
| Normal | ~4,428 | 0 | No lesions |
| Ischemic Stroke | ~1,129 | 1 | Pixel-level lesion mask (.npy) |
| Hemorrhagic Stroke | ~1,093 | 2 | Pixel-level lesion mask (.npy) |

本项目构建了目前国内规模较大的平扫CT卒中影像数据集，共计**6,650张**来自真实临床场景的512×512像素CT断层图像（PNG格式），涵盖三类：

| 类别 | 样本量 | 标签 | 标注信息 |
|------|--------|------|----------|
| 正常（Normal） | ~4,428张 | 0 | 无病灶标注 |
| 缺血性卒中（Ischemia） | ~1,129张 | 1 | 病灶像素级MASK（.npy格式） |
| 出血性卒中（Bleeding） | ~1,093张 | 2 | 病灶像素级MASK（.npy格式） |

The dataset was split using **stratified sampling** at a **70%:15%:15%** ratio (training: 4,655, validation: 997, test: 998), ensuring consistent class proportions across all subsets.

训练集/验证集/测试集按**70%:15%:15%**的比例进行分层抽样划分，其中训练集4,655张、验证集997张、测试集998张。

### 3.3 Core Technical Architecture
### 3.3 核心技术架构

#### (I) Stroke Identification Module (CerebriScan Identifier)
#### （一）卒中识别模块（CerebriScan Identifier）

The identification module adopts a **hybrid architecture combining Convolutional Mixture of Experts (ConvMoE) and Vision Transformer (ViT)**, achieving synergy between local feature extraction and global context analysis within a unified framework:

- **ConvMoE Layer**: Four convolutional expert networks with different activation functions (ReLU, Tanh, ELU, SELU) whose weights are dynamically assigned by a router, allowing the model to adaptively capture lesion features of varying morphology.
- **Patch Embedding**: CT images are divided into 32×32 non-overlapping patches, generating 896-dimensional embedding vectors with a sequence length of 257 (including a learnable class token).
- **Transformer Encoder**: Multi-head self-attention captures long-range dependencies among patches across the entire image, with SwiGLU activation enhancing non-linear representation capability.
- **Positional Encoding**: Learnable positional encodings preserve spatial location information.
- **Distributed Training**: The model was trained on 2× NVIDIA Tesla V100 (32GB) GPUs using TensorFlow MirroredStrategy, with the Adam optimizer (initial learning rate 0.001) and Sparse Categorical Crossentropy loss.

识别模块采用**卷积专家混合（Convolutional Mixture of Experts, ConvMoE）与Vision Transformer（ViT）的混合架构**，在同一框架内实现了局部特征提取与全局上下文分析的协同：
- **卷积MoE层**：分别使用ReLU、Tanh、ELU、SELU四种激活函数的卷积专家网络，通过路由器（Router）动态分配各专家的权重。
- **图像分块嵌入（Patch Embedding）**：将CT图像划分为32×32的非重叠补丁，生成896维嵌入向量。
- **Transformer编码器**：运用多头自注意力机制在全图范围内捕捉各补丁之间的长程依赖关系，配合SwiGLU激活函数。
- **位置编码（Positional Encoding）**：通过可学习的位置编码保留空间位置信息。
- **分布式训练**：模型在2× NVIDIA Tesla V100（32GB）GPU上并行训练。

**Performance**:

| Metric | Training | Validation | **Test** |
|--------|----------|------------|----------|
| Accuracy | 100% | 96.29% | **95.29%** |
| Macro F1 | 1.00 | 0.97 | **0.953** |

**Per-Class Performance on Test Set**:

| Class | Precision | Recall | F1 Score |
|-------|-----------|--------|----------|
| Normal | 0.96 | 0.98 | 0.97 |
| Ischemia | 0.93 | 0.89 | 0.91 |
| Bleeding | 0.95 | 0.88 | 0.92 |

Ablation studies confirmed that the hybrid architecture outperforms individual models in both classification accuracy and generalization.

**性能表现**：

| 指标 | 训练集 | 验证集 | **测试集** |
|------|--------|--------|-----------|
| 准确率（Accuracy） | 100% | 96.29% | **95.29%** |
| 宏平均F1（Macro F1） | 1.00 | 0.97 | **0.953** |

**测试集各类别详细表现**：

| 类别 | 精确率（Precision） | 召回率（Recall） | F1分数 |
|------|-------------------|-----------------|--------|
| 正常（Normal） | 0.96 | 0.98 | 0.97 |
| 缺血性卒中（Ischemia） | 0.93 | 0.89 | 0.91 |
| 出血性卒中（Bleeding） | 0.95 | 0.88 | 0.92 |

#### (II) Stroke Segmentation Module
#### （二）卒中分割模块（Stroke Segmentation Module）

The segmentation module performs pixel-level lesion segmentation for both hemorrhagic and ischemic stroke using the classic **U-Net architecture** (encoder-decoder structure with skip connections). Input: 512×512×3 CT images; output: pixel-level segmentation probability maps.

- **U-Net Encoder**: Progressive downsampling to extract multi-scale lesion features.
- **U-Net Decoder**: Transposed convolution for progressive upsampling, with skip connections to corresponding encoder layers for precise localization.
- **Loss Function**: A hybrid loss combining binary cross-entropy and Dice coefficient (BCE-Dice Loss) to balance pixel-level classification accuracy and lesion region overlap.
- **Performance**: Hemorrhage segmentation on the test set achieved **Mean IoU of 84.22%**, **pixel accuracy of 99.63%**, and **lesion region IoU of approximately 69.79%**, validating the effectiveness of this method for precise lesion localization.

The project also explored **TransUNet** (integrating Transformer with U-Net) to further enhance long-range spatial dependency modeling.

分割模块采用经典的**U-Net架构**对病灶区域进行像素级精确分割。
- **U-Net编码器**：逐层下采样提取病灶的多尺度特征。
- **U-Net解码器**：通过转置卷积逐层上采样恢复图像分辨率，并与对应编码器层跳跃连接。
- **损失函数**：结合二分类交叉熵与Dice系数的混合损失函数（BCE-Dice Loss）。
- **性能**：出血灶分割在测试集上达到**Mean IoU 84.22%**、**像素准确率99.63%**、**病灶区域IoU约69.79%**。

此外，项目还探索了**TransUNet**在卒中分割任务中的应用。

### 3.4 Project Highlights and Innovations
### 3.4 项目特色与创新点

1. **ConvMoE + ViT Hybrid Architecture**: Pioneering integration of convolutional mixture of experts with Vision Transformer in medical image classification, combining fine-grained local texture capture with global context modeling.

2. **Dual-Task Synergy (Identification + Segmentation)**: The system simultaneously performs three-class stroke classification and lesion segmentation — the former provides rapid diagnostic decision support, while the latter offers quantitative lesion extent information, forming a complete "identify first, localize next" workflow.

3. **Non-Contrast CT as Entry Point**: NCCT is the first-line imaging modality for emergency stroke assessment. Using it as the sole input ensures clinical accessibility and deployment feasibility, especially in primary care hospitals.

4. **MRF Preprocessing Exploration**: The project also explored Gaussian Mixture Model (GMM)-based Markov Random Field (MRF) segmentation for CT image preprocessing, providing multi-path technical reserves for future model optimization.

1. **ConvMoE + ViT混合架构**：在医学影像分类任务中首次将卷积专家混合与Vision Transformer相结合。
2. **识别与分割双任务协同**：系统在同一平台内同时实现卒中三分类与病灶区域分割，形成"先识别、后定位"的完整工作流。
3. **平扫CT为切入点**：以NCCT作为系统唯一输入模态，确保临床可及性和推广可能性。
4. **马尔科夫随机场（MRF）预处理探索**：尝试基于GMM+空间约束的MRF图像分割方法进行CT图像预处理。

### 3.5 Clinical Value and Application Prospects
### 3.5 临床价值与应用前景

With a three-class classification accuracy of **95.29%** and a lesion segmentation Mean IoU exceeding 84%, CerebraScan demonstrates strong clinical application potential:

- **Assisting Emergency Decision-Making**: Intelligent analysis of NCCT within seconds, helping emergency and neurology physicians rapidly determine stroke type and lesion extent, reducing Door-to-Needle Time.
- **Reducing Missed Diagnosis and Misdiagnosis**: Particularly valuable for cases where early ischemic signs or posterior circulation infarcts are difficult to identify visually.
- **Quantitative Assessment Support**: The segmentation module provides precise volume and location information of hematomas/infarcts, offering quantitative evidence for prognosis evaluation and treatment planning.
- **Potential for Primary Care Deployment**: The system requires only NCCT as input, without reliance on advanced imaging equipment (MRI, CTP, CTA), facilitating deployment in primary care hospitals and stroke center networks.

CerebraScan系统在测试集上对卒中三分类的准确率达**95.29%**，病灶分割Mean IoU超过84%，展现了良好的临床应用潜力：
- **辅助急诊快速决策**：可在秒级时间内对平扫CT进行智能分析，缩短"门到针"时间。
- **降低漏诊与误诊率**：尤其对超早期缺血性卒中和后循环梗死等肉眼识别困难的病例。
- **量化评估支持**：病灶分割模块提供血肿/梗死灶的精确体积和位置信息。
- **基层医院推广潜力**：系统仅需平扫CT作为输入，有利于在基层医院和卒中中心网络中推广部署。

---

*CerebraScan will continue to evolve. Future plans include multi-center prospective clinical validation and further exploration of multimodal imaging data integration (CTP, MRI) for more comprehensive and accurate AI-assisted stroke diagnosis.*

*CerebraScan项目将持续迭代，未来计划纳入多中心前瞻性临床验证，并进一步探索CT灌注成像（CTP）和磁共振（MRI）等多模态影像数据的融合分析。*
