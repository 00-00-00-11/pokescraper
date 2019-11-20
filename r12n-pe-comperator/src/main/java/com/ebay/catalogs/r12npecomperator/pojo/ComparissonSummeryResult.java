package com.ebay.catalogs.r12npecomperator.pojo;

import jdk.jfr.DataAmount;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class ComparissonSummeryResult {
  private final int numberOfConvertedEpids;
  private final int numberOfFailedEpids;
  private final String outputFileFullPathName;
}
