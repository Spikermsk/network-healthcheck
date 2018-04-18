package com.devnetcreate.ncheckdaily.nethealthcheckdaily;

import com.google.gson.annotations.SerializedName;

public class WanAvailability {

    @SerializedName("total_time")
    public String total_time;

    @SerializedName("up")
    public String up;

    @SerializedName("down")
    public String down;
}
