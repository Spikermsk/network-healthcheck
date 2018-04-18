package com.devnetcreate.ncheckdaily.nethealthcheckdaily;

import com.google.gson.annotations.SerializedName;

public class Sla {

    @SerializedName("device_availability")
    public String device_availability;

    @SerializedName("uptime")
    public String uptime;

    @SerializedName("problem_detected")
    public String problem_detected;

    @SerializedName("critical_status")
    public String critical_status;
}
