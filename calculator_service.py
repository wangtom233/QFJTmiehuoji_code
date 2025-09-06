def calculate_specific_volume(temperature):
    """
    计算比容 S = 0.0664 + 0.000274 × T
    :param temperature: 环境温度 (°C), 必须 <= 30°C
    :return: 比容 (m³/kg)
    """
    if temperature > 30:
        raise ValueError("环境温度不能超过30°C。")
    return 0.0664 + 0.000274 * temperature
    # return 0.1269 + 0.000513 * temperature #计算七氟丙烷，验证程序逻辑

def calculate_agent_mass(volume, concentration, temperature):
    """
    计算全氟己酮质量 m = c × v / (S × (100 - c))
    :param volume: 防护区体积 (m³)
    :param concentration: 设计浓度 (%), 必须 < 100%
    :param temperature: 环境温度 (°C)
    :return: 全氟己酮质量 (kg)
    """
    if concentration >= 100:
        raise ValueError("设计浓度必须小于100%。")

    S = calculate_specific_volume(temperature)
    numerator = concentration * volume
    denominator = S * (100 - concentration)
    return numerator / denominator


def calculate_required_volume(mass, density, filling_ratio):
    """
    计算防护区域所需体积 V = m / (p * d)
    :param mass: 所需灭火剂质量 (kg)
    :param density: 全氟己酮密度 (kg/m³)
    :param filling_ratio: 充装率, 默认0.85
    :return: 灭火器所需体积 (m³)
    """
    if mass <= 0:
        raise ValueError("所需灭火剂质量必须大于0 kg。")
    if density <= 0:
        raise ValueError("全氟己酮密度必须大于0 kg/m³。")
    if filling_ratio <= 0 or filling_ratio > 1:
        raise ValueError("充装率必须在0到1之间。")

    required_volume = 1000 *mass / (density * filling_ratio)
    return required_volume

"""
if __name__ == '__main__':
    # 示例调用
    try:
        v = 12.56  # 防护区域体积 (m³)
        c = 9  # 设计浓度 (%)
        T = 20  # 环境温度 (°C)
        p = 1120  # 全氟己酮密度 (kg/m³)
        d = 0.85  # 充装率

        mass = calculate_agent_mass(v, c, T)
        volume = calculate_required_volume(mass, p, d)
        print(f"所需灭火剂质量: {mass:.3f} kg")
        print(f"所需灭火器体积: {volume:.3f} 升")
    except ValueError as e:
        print(e)
"""