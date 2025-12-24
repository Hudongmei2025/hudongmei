# setup.py
import os
import subprocess
import sys

def setup_environment():
    print("正在设置中文字体环境...")
    
    # 安装必要的包
    packages = [
        'matplotlib',
        'fonttools',
        'Pillow'
    ]
    
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"安装 {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    # 配置 matplotlib 使用中文字体
    import matplotlib
    matplotlib.use('Agg')  # 使用非交互式后端
    
    # 尝试多种字体配置
    font_configs = [
        {'font.sans-serif': ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS'],
         'axes.unicode_minus': False},
        {'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
         'axes.unicode_minus': False}
    ]
    
    for config in font_configs:
        try:
            matplotlib.rcParams.update(config)
            print(f"字体配置成功: {config['font.sans-serif'][0]}")
            break
        except:
            continue
    
    print("环境设置完成！")

if __name__ == "__main__":
    setup_environment()