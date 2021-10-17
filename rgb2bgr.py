def rbg2bgr(n):
    return 0x10000 * (n & 0x0000ff) + 0x100 * (n >> 8 & 0x0000ff) + (n >> 16 & 0x0000ff)
