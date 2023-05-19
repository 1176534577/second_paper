***执行步骤
1. 执行combine4to1从原生数据生成obs
2. 执行main_paper生成ijg文件和ray_way_j文件
3. 执行最外层的main生成结果



***四个数据集
- dataset1数据集1，外部2.65，内部1  
- dataset2数据集2，外部2.65，内部1  
- dataset3数据集3，外部2.65，内部1  
- dataset4数据集4，外部2.65，内部1  

***数据文件夹结构  
- RawData原始数据  
    - dataset1  
        - 探测器坐标  
        - 探测器1的数据  
        - 探测器2的数据  
        - 探测器3的数据  
        - 探测器4的数据  
    - dataset2 同dataset1结构  
    - dataset3 同dataset1结构  
    - dataset4 同dataset1结构  
- input输入数据  
    - dataset1  
        - obs文件
        - mesh文件
    - dataset2 同dataset1结构  
    - dataset3 同dataset1结构  
    - dataset4 同dataset1结构  
- output输出数据
    - dataset1
        - ijg(射线编号，体素编号，体素实际长度)
        - ray_way_j(射线的等效长度)
        - MyAlgorithm 所提算法
            - noise free 无噪声
              - YYYY_MM_DD_HH_mm_ss 以年_月_日_时_分_秒为文件夹命名
                - res 算法的直接结果(常用)，参与到计算的体素，不含空气体素及未被射线穿过(不参与到计算)的体素
                - big_norm 大二范数
                - small_norm 小二范数
                - all_res 所有格子的密度值(可视化使用)
                - res_without_air 不含空气的密度值
              - YYYY_MM_DD_HH_mm_ss 以年_月_日_时_分_秒为文件夹命名
              - YYYY_MM_DD_HH_mm_ss 以年_月_日_时_分_秒为文件夹命名
              - YYYY_MM_DD_HH_mm_ss 以年_月_日_时_分_秒为文件夹命名
              - YYYY_MM_DD_HH_mm_ss 以年_月_日_时_分_秒为文件夹命名
            - noise constant 常量噪声
            - noise random 随机噪声
        - CG 共轭梯度法
        - GA 遗传算法
        - SA 模拟退火法
    - dataset2 同dataset1  
    - dataset3 同dataset1  
    - dataset4 同dataset1  