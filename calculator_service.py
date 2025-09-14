def calculate_specific_volume_fluoroketone(temperature):
    """
    计算全氟己酮的比容 S_1 = 0.0664 + 0.000274 × T
    :param temperature: 环境温度 (°C), 必须 <= 30°C
    :return: 比容 (m³/kg)
    """
    if temperature > 30:
        raise ValueError("环境温度不能超过30°C。")
    return 0.0664 + 0.000274 * temperature


def calculate_specific_volume_hfc(temperature):
    """
    计算七氟丙烷的比容 S_2 = 0.1269 + 0.000513 × T
    :param temperature: 环境温度 (°C), 必须 <= 30°C
    :return: 比容 (m³/kg)
    """
    if temperature > 30:
        raise ValueError("环境温度不能超过30°C。")
    return 0.1269 + 0.000513 * temperature


def calculate_agent_mass_fluoroketone(volume_1, concentration, temperature):
    """
    计算全氟己酮的质量 m =  c × v / (S_1 × (100 - c))
    :param volume_1: 防护区体积 (m³)
    :param concentration: 设计浓度 (%), 必须 < 100%
    :param temperature: 环境温度 (°C)
    :return: 全氟己酮质量 (kg)
    """
    if concentration >= 100:
        raise ValueError("设计浓度必须小于100%。")

    s_1 = calculate_specific_volume_fluoroketone(temperature)
    numerator = concentration * volume_1
    denominator = s_1 * (100 - concentration)
    return numerator / denominator


def calculate_agent_mass_hfc(volume_2, concentration, temperature, altitude_coefficient=1.0):
    """
    计算七氟丙烷的质量 m =  c × v / (S_2 × (100 - c))
    :param volume_2: 防护区体积 (m³)
    :param concentration: 设计浓度 (%), 必须 < 100%
    :param temperature: 环境温度 (°C)
    :param altitude_coefficient: 海拔修正系数，默认值1.0
    :return: 七氟丙烷质量 (kg)
    """
    if concentration >= 100:
        raise ValueError("设计浓度必须小于100%。")

    s_2 = calculate_specific_volume_hfc(temperature)
    numerator = altitude_coefficient * concentration * volume_2
    denominator = s_2 * (100 - concentration)
    return numerator / denominator


def calculate_required_volume(mass, density, filling_ratio):
    """
    计算防护区域所需体积 V = m / (p * d)
    :param mass: 所需灭火剂质量 (kg)
    :param density: 灭火剂密度 (kg/m³)
    :param filling_ratio: 充装率, 默认0.85
    :return: 灭火器所需体积 (L)
    """
    if mass <= 0:
        raise ValueError("所需灭火剂质量必须大于0 kg。")
    if density <= 0:
        raise ValueError("灭火剂密度必须大于0 kg/m³。")
    if filling_ratio <= 0 or filling_ratio > 1:
        raise ValueError("充装率必须在0到1之间。")

    required_volume = 1000 * mass / (density * filling_ratio)
    return required_volume
"""
if __name__ == '__main__':
    # 示例调用
    try:
        v = 12.56  # 防护区域体积 (m³)
        c = 9  # 设计浓度 (%)
        T = 20  # 环境温度 (°C)
        p_1 = 1120  # 七氟丙烷密度 (kg/m³)
        p_2 = 1420   # 全氟己酮度 (kg/m³)
        d = 0.85  # 充装率
        k =1.0  #海拔修正系数
        #七氟丙烷
        #mass = calculate_agent_mass_hfc(v, c, T,k) 
        #全氟己酮
        mass = calculate_agent_mass_fluoroketone(v, c, T)
        #容量
        volume = calculate_required_volume(mass, p_1, d)
        print(f"所需灭火剂质量: {mass:.2f} kg")
        print(f"所需灭火器体积: {volume:.2f} 升")
    except ValueError as e:
        print(e)
"""