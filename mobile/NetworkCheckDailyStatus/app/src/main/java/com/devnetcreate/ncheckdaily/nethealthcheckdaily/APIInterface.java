package com.devnetcreate.ncheckdaily.nethealthcheckdaily;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Query;

public interface APIInterface {

    @GET("/api/v2/cio/stats")
    Call<Status> getStats();

    @GET("/api/v2/cio/slas")
    Call<Sla> getlas();

    @GET("/api/v2/director/ticketstatus")
    Call<TicketStatus> getticketStatus();

    @GET("/api/v2/manager/availability")
    Call<WanAvailability> getWanAvailability();
}
