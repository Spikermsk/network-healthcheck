package com.devnetcreate.ncheckdaily.nethealthcheckdaily;

import com.google.gson.annotations.SerializedName;

public class Status {

    @SerializedName("error")
    public String error;

    @SerializedName("warning")
    public String warning;

    @SerializedName("ok")
    public String ok;

    @SerializedName("inactive")
    public String inactive;

}
