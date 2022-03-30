from check_output import *

src = "keepgoing_multi_step.sv"

for task in ["keepgoing_multi_step_bmc", "keepgoing_multi_step_prove"]:
    assert_0 = line_ref(task, src, "assert(0)")
    step_3_7 = line_ref(task, src, "step 3,7")
    step_5 = line_ref(task, src, "step 5")
    step_7 = line_ref(task, src, "step 7")

    log = open(task + "/logfile.txt").read()
    log_per_trace = log.split("Writing trace to VCD file")[:-1]

    assert len(log_per_trace) == 4


    assert re.search(r"Assert failed in test: %s \(.*\)$" % assert_0, log_per_trace[0], re.M)

    for i in range(1, 4):
        assert re.search(r"Assert failed in test: %s \(.*\) \[failed before\]$" % assert_0, log_per_trace[i], re.M)


    assert re.search(r"Assert failed in test: %s \(.*\)$" % step_3_7, log_per_trace[1], re.M)
    assert re.search(r"Assert failed in test: %s \(.*\)$" % step_5, log_per_trace[2], re.M)
    assert re.search(r"Assert failed in test: %s \(.*\) \[failed before\]$" % step_3_7, log_per_trace[3], re.M)
    assert re.search(r"Assert failed in test: %s \(.*\)$" % step_7, log_per_trace[3], re.M)

