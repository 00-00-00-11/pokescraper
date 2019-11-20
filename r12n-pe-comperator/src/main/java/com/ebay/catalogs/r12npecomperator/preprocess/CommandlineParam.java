package com.ebay.catalogs.r12npecomperator.preprocess;

public enum CommandlineParam {
  INPUT_FILE_PATH("INPUT_FILE_PATH"),
  OUTPUT_FILES_PATH("OUTPUT_FILES_PATH"),
  CHUNK_SIZE("CHUNK_SIZE", "100"),
  RECOVERY_MODE("RECOVERY_MODE", "false");

  private String paramName;
  private String defaultValue;

  CommandlineParam(String paramName, String defaultValue) {
    this.paramName = paramName;
    this.defaultValue = defaultValue;

  }

  CommandlineParam(String paramName) {
    this.paramName = paramName;
    this.defaultValue = null;

  }

  public String getParamName() {
    return paramName;
  }

  public String getDefaultValue() {
    return defaultValue;
  }
}
