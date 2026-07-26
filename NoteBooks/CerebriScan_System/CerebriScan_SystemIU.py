#CerebriScan_system系统UI界面
import sys
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QSlider, QCheckBox, QGroupBox, QFrame,
                             QSplitter, QComboBox, QToolBar, QAction, QStatusBar)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QColor, QPalette

# 设置matplotlib中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

class MedicalImageCanvas(FigureCanvas):
    """医学图像显示画布"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor='black')
        self.axes = self.fig.add_subplot(111)
        self.axes.set_facecolor('black')
        super().__init__(self.fig)
        self.setParent(parent)
        
        # 初始化图像数据
        self.image_data = None
        self.current_slice = 0
        self.window_level = 40
        self.window_width = 400
        
        # 隐藏坐标轴
        self.axes.axis('off')
        self.fig.tight_layout(pad=0)
        
    def set_image(self, image_data):
        """设置图像数据"""
        self.image_data = image_data
        self.update_display()
        
    def set_slice(self, slice_idx):
        """设置当前切片"""
        if self.image_data is not None and 0 <= slice_idx < self.image_data.shape[0]:
            self.current_slice = slice_idx
            self.update_display()
            
    def set_window(self, level, width):
        """设置窗宽窗位"""
        self.window_level = level
        self.window_width = width
        self.update_display()
        
    def update_display(self):
        """更新显示"""
        if self.image_data is None:
            return
            
        self.axes.clear()
        self.axes.axis('off')
        
        # 获取当前切片
        slice_data = self.image_data[self.current_slice, :, :]
        
        # 应用窗宽窗位
        lower = self.window_level - self.window_width / 2
        upper = self.window_level + self.window_width / 2
        slice_data = np.clip(slice_data, lower, upper)
        
        # 归一化到0-1
        slice_data = (slice_data - lower) / (upper - lower)
        
        # 显示图像
        self.axes.imshow(slice_data, cmap='gray', origin='upper')
        
        # 添加十字线
        h, w = slice_data.shape
        self.axes.axhline(y=h//2, color='yellow', linewidth=0.5)
        self.axes.axvline(x=w//2, color='yellow', linewidth=0.5)
        
        self.fig.canvas.draw_idle()

class MedicalImageViewer(QMainWindow):
    """医学影像查看器主窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("医学影像AI辅助诊断系统")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QWidget {
                color: #ffffff;
                font-family: "Microsoft YaHei", sans-serif;
            }
            QPushButton {
                background-color: #2d2d2d;
                border: 1px solid #444444;
                padding: 6px 12px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3d3d3d;
            }
            QPushButton:pressed {
                background-color: #4d4d4d;
            }
            QSlider::groove:horizontal {
                background: #3d3d3d;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #0078d7;
                width: 16px;
                margin: -4px 0;
                border-radius: 8px;
            }
            QGroupBox {
                border: 1px solid #444444;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QCheckBox {
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 1px solid #444444;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked {
                background-color: #0078d7;
                border-color: #0078d7;
            }
        """)
        
        # 生成模拟的CT数据
        self.generate_dummy_data()
        
        # 创建UI
        self.create_toolbar()
        self.create_central_widget()
        self.create_status_bar()
        
        # 初始化显示
        self.update_all_views()
        
    def generate_dummy_data(self):
        """生成模拟的CT数据"""
        # 创建3D数组模拟CT数据
        self.axial_data = np.zeros((200, 256, 256), dtype=np.float32)
        self.coronal_data = np.zeros((200, 256, 256), dtype=np.float32)
        self.sagittal_data = np.zeros((200, 256, 256), dtype=np.float32)
        
        # 添加模拟的主动脉和病变
        for i in range(200):
            # 轴位视图
            y, x = np.ogrid[:256, :256]
            center_x, center_y = 128, 100
            radius = 15 + 5 * np.sin(i * 0.05)
            
            # 主动脉
            dist_from_center = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            self.axial_data[i, dist_from_center < radius] = 40
            self.axial_data[i, (dist_from_center < radius-3) & (dist_from_center > radius-6)] = 80
            
            # 添加模拟的夹层
            if 50 < i < 150:
                angle = np.arctan2(y - center_y, x - center_x)
                self.axial_data[i, (dist_from_center < radius) & (np.abs(angle - 0.5) < 0.2)] = 100
                
            # 背景和骨骼
            self.axial_data[i, :, :] += np.random.normal(0, 5, (256, 256))
            self.axial_data[i, 50:200, 50:200] += -100  # 肺部
            self.axial_data[i, 200:220, 120:136] = 300  # 脊柱
            
        # 生成冠状位和矢状位数据
        self.coronal_data = np.transpose(self.axial_data, (1, 0, 2))
        self.sagittal_data = np.transpose(self.axial_data, (2, 0, 1))
        
    def create_toolbar(self):
        """创建工具栏"""
        toolbar = QToolBar("主工具栏")
        toolbar.setIconSize(QSize(24, 24))
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # 添加工具按钮
        cross_action = QAction("Cross", self)
        cross_action.setCheckable(True)
        cross_action.setChecked(True)
        toolbar.addAction(cross_action)
        
        levels_action = QAction("Levels", self)
        levels_action.setCheckable(True)
        toolbar.addAction(levels_action)
        
        markup_action = QAction("Markup", self)
        markup_action.setCheckable(True)
        toolbar.addAction(markup_action)
        
        toolbar.addSeparator()
        
        exit_2d_action = QAction("Exit 2D MPR", self)
        toolbar.addAction(exit_2d_action)
        
        show_hide_action = QAction("Show or Hide", self)
        toolbar.addAction(show_hide_action)
        
        toolbar.addSeparator()
        
        # 添加右侧按钮
        toolbar.addWidget(QWidget())  # 占位符
        help_action = QAction("Help", self)
        toolbar.addAction(help_action)
        
        vertical_action = QAction("Vertical Screen", self)
        toolbar.addAction(vertical_action)
        
    def create_central_widget(self):
        """创建中央部件"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)
        
        # 创建图像显示区域
        image_container = QWidget()
        image_layout = QVBoxLayout(image_container)
        image_layout.setContentsMargins(0, 0, 0, 0)
        image_layout.setSpacing(5)
        
        # 上排两个视图
        top_row = QHBoxLayout()
        top_row.setSpacing(5)
        
        # 轴位视图
        self.axial_canvas = MedicalImageCanvas(width=6, height=6)
        self.axial_canvas.set_image(self.axial_data)
        top_row.addWidget(self.axial_canvas, 1)
        
        # 冠状位视图
        self.coronal_canvas = MedicalImageCanvas(width=6, height=6)
        self.coronal_canvas.set_image(self.coronal_data)
        top_row.addWidget(self.coronal_canvas, 1)
        
        image_layout.addLayout(top_row, 1)
        
        # 下排两个视图
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(5)
        
        # 矢状位视图
        self.sagittal_canvas = MedicalImageCanvas(width=6, height=6)
        self.sagittal_canvas.set_image(self.sagittal_data)
        bottom_row.addWidget(self.sagittal_canvas, 1)
        
        # AI结果视图
        self.ai_canvas = MedicalImageCanvas(width=6, height=6)
        # 创建模拟的AI热图
        ai_data = np.zeros((200, 256, 256), dtype=np.float32)
        for i in range(200):
            y, x = np.ogrid[:256, :256]
            center_x, center_y = 128, 100
            dist_from_center = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            ai_data[i, dist_from_center < 20] = 1.0
            ai_data[i, :, :] *= np.exp(-((i - 100)**2) / 2000)
            
        self.ai_canvas.set_image(ai_data)
        self.ai_canvas.axes.imshow(ai_data[100, :, :], cmap='jet', alpha=0.7, origin='upper')
        bottom_row.addWidget(self.ai_canvas, 1)
        
        image_layout.addLayout(bottom_row, 1)
        
        main_layout.addWidget(image_container, 3)
        
        # 创建右侧控制面板
        control_panel = QWidget()
        control_panel.setMaximumWidth(300)
        control_layout = QVBoxLayout(control_panel)
        control_layout.setContentsMargins(10, 10, 10, 10)
        control_layout.setSpacing(15)
        
        # AI结果显示
        ai_group = QGroupBox("AI 辅助诊断结果")
        ai_layout = QVBoxLayout(ai_group)
        
        # 显示AI掩码复选框
        self.show_ai_mask = QCheckBox("Show AI Mask")
        self.show_ai_mask.setChecked(True)
        ai_layout.addWidget(self.show_ai_mask)
        
        # 不透明度滑块
        opacity_layout = QHBoxLayout()
        opacity_layout.addWidget(QLabel("Opacity:"))
        self.opacity_slider = QSlider(Qt.Horizontal)
        self.opacity_slider.setRange(0, 100)
        self.opacity_slider.setValue(70)
        opacity_layout.addWidget(self.opacity_slider)
        ai_layout.addLayout(opacity_layout)
        
        # 诊断结果
        result_frame = QFrame()
        result_frame.setStyleSheet("background-color: #2d2d2d; border-radius: 6px; padding: 10px;")
        result_layout = QVBoxLayout(result_frame)
        
        aas_label = QLabel("AAS")
        aas_label.setAlignment(Qt.AlignCenter)
        aas_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        result_layout.addWidget(aas_label)
        
        abnormal_label = QLabel("Abnormal")
        abnormal_label.setAlignment(Qt.AlignCenter)
        abnormal_label.setStyleSheet("color: #ff4444; font-weight: bold;")
        result_layout.addWidget(abnormal_label)
        
        result_layout.addSpacing(10)
        
        prob_button = QPushButton("Abnormal probability of AAS: 100%")
        prob_button.setStyleSheet("background-color: #0078d7; color: white; font-weight: bold;")
        result_layout.addWidget(prob_button)
        
        conclusion_label = QLabel("Conclusion: Presence of Acute Aortic Syndrome")
        conclusion_label.setWordWrap(True)
        conclusion_label.setAlignment(Qt.AlignCenter)
        result_layout.addWidget(conclusion_label)
        
        ai_layout.addWidget(result_frame)
        
        control_layout.addWidget(ai_group)
        
        # 图像控制
        image_control_group = QGroupBox("图像控制")
        image_control_layout = QVBoxLayout(image_control_group)
        
        # 切片滑块
        slice_layout = QHBoxLayout()
        slice_layout.addWidget(QLabel("切片:"))
        self.slice_slider = QSlider(Qt.Horizontal)
        self.slice_slider.setRange(0, 199)
        self.slice_slider.setValue(100)
        self.slice_slider.valueChanged.connect(self.on_slice_changed)
        slice_layout.addWidget(self.slice_slider)
        self.slice_label = QLabel("100/200")
        slice_layout.addWidget(self.slice_label)
        image_control_layout.addLayout(slice_layout)
        
        # 窗宽窗位
        wl_layout = QHBoxLayout()
        wl_layout.addWidget(QLabel("窗位:"))
        self.wl_slider = QSlider(Qt.Horizontal)
        self.wl_slider.setRange(-1000, 1000)
        self.wl_slider.setValue(40)
        self.wl_slider.valueChanged.connect(self.on_window_changed)
        wl_layout.addWidget(self.wl_slider)
        self.wl_label = QLabel("40")
        wl_layout.addWidget(self.wl_label)
        image_control_layout.addLayout(wl_layout)
        
        ww_layout = QHBoxLayout()
        ww_layout.addWidget(QLabel("窗宽:"))
        self.ww_slider = QSlider(Qt.Horizontal)
        self.ww_slider.setRange(1, 2000)
        self.ww_slider.setValue(400)
        self.ww_slider.valueChanged.connect(self.on_window_changed)
        ww_layout.addWidget(self.ww_slider)
        self.ww_label = QLabel("400")
        ww_layout.addWidget(self.ww_label)
        image_control_layout.addLayout(ww_layout)
        
        # 预设窗宽窗位
        preset_layout = QHBoxLayout()
        preset_layout.addWidget(QLabel("预设:"))
        self.preset_combo = QComboBox()
        self.preset_combo.addItems(["软组织", "肺", "骨", "脑"])
        self.preset_combo.currentIndexChanged.connect(self.on_preset_changed)
        preset_layout.addWidget(self.preset_combo)
        image_control_layout.addLayout(preset_layout)
        
        control_layout.addWidget(image_control_group)
        
        # 患者信息
        patient_group = QGroupBox("患者信息")
        patient_layout = QVBoxLayout(patient_group)
        
        patient_info = [
            "姓名: N20_PATIENT",
            "性别: **",
            "年龄: **",
            "检查日期: **",
            "检查号: Fig3a_visable"
        ]
        
        for info in patient_info:
            label = QLabel(info)
            patient_layout.addWidget(label)
            
        control_layout.addWidget(patient_group)
        
        # 免责声明
        disclaimer_label = QLabel("产品结果仅供医生参考，不作为最终临床诊断依据。")
        disclaimer_label.setWordWrap(True)
        disclaimer_label.setStyleSheet("color: #aaaaaa; font-size: 10px;")
        control_layout.addWidget(disclaimer_label)
        
        control_layout.addStretch()
        
        main_layout.addWidget(control_panel, 1)
        
    def create_status_bar(self):
        """创建状态栏"""
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("就绪")
        
    def on_slice_changed(self, value):
        """切片改变事件"""
        self.slice_label.setText(f"{value}/200")
        self.update_all_views()
        
    def on_window_changed(self):
        """窗宽窗位改变事件"""
        level = self.wl_slider.value()
        width = self.ww_slider.value()
        self.wl_label.setText(str(level))
        self.ww_label.setText(str(width))
        
        self.axial_canvas.set_window(level, width)
        self.coronal_canvas.set_window(level, width)
        self.sagittal_canvas.set_window(level, width)
        
    def on_preset_changed(self, index):
        """预设窗宽窗位改变事件"""
        presets = [
            (40, 400),    # 软组织
            (-600, 1500), # 肺
            (400, 2000),  # 骨
            (40, 80)      # 脑
        ]
        
        level, width = presets[index]
        self.wl_slider.setValue(level)
        self.ww_slider.setValue(width)
        
    def update_all_views(self):
        """更新所有视图"""
        slice_idx = self.slice_slider.value()
        self.axial_canvas.set_slice(slice_idx)
        self.coronal_canvas.set_slice(slice_idx)
        self.sagittal_canvas.set_slice(slice_idx)
        self.ai_canvas.set_slice(slice_idx)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MedicalImageViewer()
    window.show()
    sys.exit(app.exec_())