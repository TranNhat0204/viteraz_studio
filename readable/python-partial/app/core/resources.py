# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/resources.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: MachineProfile.to_dict
def to_dict(self):
    return asdict(self)



# NOT DECOMPILED: ram_info_mb


# NOT DECOMPILED: _nvidia_smi


# NOT DECOMPILED: gpu_static


# NOT DECOMPILED: gpu_dynamic


# Original qualified name: _suggest_from
def _suggest_from(cpu_count, ram_total_mb, vram_mb, has_cuda):
    cpu_slots = max(2, min(cpu_count // 2, 8))
    if ram_total_mb:
        cpu_slots = max(2, min(cpu_slots, ram_total_mb // 1536))
    net_slots = max(4, min(cpu_count, 12))
    if has_cuda:
        if vram_mb <= 0:
            return {gpu_slots: 1, net_slots: net_slots, cpu_slots: cpu_slots,
                gpu_concurrency: 1, whisper_batch_size: 1, whisper_cpu_threads:
                max(4, min(cpu_count, 12))}
    else:
        return {gpu_slots: 1, net_slots: net_slots, cpu_slots: cpu_slots,
            gpu_concurrency: 1, whisper_batch_size: 1, whisper_cpu_threads: max
            (4, min(cpu_count, 12))}
    if vram_mb >= 12000:
        __temp_227758, __temp_227759, __temp_227760 = 3, 3, 24
        gpu_slots = __temp_227758
        gpu_conc = __temp_227759
        batch = __temp_227760
    elif vram_mb >= 8000:
        __temp_227761, __temp_227762, __temp_227763 = 3, 2, 16
        gpu_slots = __temp_227761
        gpu_conc = __temp_227762
        batch = __temp_227763
    elif vram_mb >= 6000:
        __temp_227764, __temp_227765, __temp_227766 = 2, 2, 8
        gpu_slots = __temp_227764
        gpu_conc = __temp_227765
        batch = __temp_227766
    elif vram_mb >= 4000:
        __temp_227767, __temp_227768, __temp_227769 = 1, 1, 4
        gpu_slots = __temp_227767
        gpu_conc = __temp_227768
        batch = __temp_227769
    else:
        __temp_227770, __temp_227771, __temp_227772 = 1, 1, 1
        gpu_slots = __temp_227770
        gpu_conc = __temp_227771
        batch = __temp_227772
    if ram_total_mb:
        ram_cap = max(1, int((ram_total_mb - 4096) // 2560))
        if not ram_cap < gpu_conc:
            if ram_cap < gpu_slots:
                log.info('[resources] RAM ' + str(ram_total_mb) +
                    'MB giới hạn số tác vụ song song xuống ' + str(ram_cap) +
                    ' (VRAM ' + str(vram_mb) + 'MB cho phép gpu_conc=' + str(
                    gpu_conc) + ', gpu_slots=' + str(gpu_slots) + ').')
                gpu_conc = min(gpu_conc, ram_cap)
            else:
                gpu_conc = min(gpu_conc, ram_cap)
        else:
            log.info('[resources] RAM ' + str(ram_total_mb) +
                'MB giới hạn số tác vụ song song xuống ' + str(ram_cap) +
                ' (VRAM ' + str(vram_mb) + 'MB cho phép gpu_conc=' + str(
                gpu_conc) + ', gpu_slots=' + str(gpu_slots) + ').')
            gpu_conc = min(gpu_conc, ram_cap)
        gpu_slots = min(gpu_slots, ram_cap)
    return {gpu_slots: gpu_slots, net_slots: net_slots, cpu_slots: cpu_slots,
        gpu_concurrency: gpu_conc, whisper_batch_size: batch,
        whisper_cpu_threads: max(4, min(cpu_count // 2, 8))}



# NOT DECOMPILED: machine_profile


# NOT DECOMPILED: snapshot


# Original qualified name: ram_pressure
def ram_pressure(min_free_mb, min_free_pct):
    __temp_227832, __temp_227833 = ram_info_mb()
    total = __temp_227832
    avail = __temp_227833
    if not total:
        return False
    return avail < max(min_free_mb, total * min_free_pct / 100.0)

