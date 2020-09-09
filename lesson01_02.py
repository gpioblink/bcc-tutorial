from bcc import BPF
BPF(text='int kprobe__sys_sync(void *ctx) { bpf_trace_printk("Hello, sys_sync world!\\n"); return 0; }').trace_print()
