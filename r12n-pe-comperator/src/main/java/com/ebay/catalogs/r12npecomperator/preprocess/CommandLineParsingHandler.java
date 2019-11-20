package com.ebay.catalogs.r12npecomperator.preprocess;

import static com.ebay.catalogs.r12npecomperator.preprocess.CommandlineParam.CHUNK_SIZE;
import static com.ebay.catalogs.r12npecomperator.preprocess.CommandlineParam.INPUT_FILE_PATH;
import static com.ebay.catalogs.r12npecomperator.preprocess.CommandlineParam.OUTPUT_FILES_PATH;
import static com.ebay.catalogs.r12npecomperator.preprocess.CommandlineParam.RECOVERY_MODE;

import javax.annotation.PostConstruct;
import org.springframework.boot.ApplicationArguments;

public class CommandLineParsingHandler {

  private String inputFilePath;
  private String outputFilePath;
  private int chunkSize;
  private boolean recoveryMode;

  private final ApplicationArguments applicationArguments;

  public CommandLineParsingHandler(ApplicationArguments applicationArguments) {
    this.applicationArguments = applicationArguments;
  }

  @PostConstruct
  void parseParams() {
    inputFilePath = extractFirst(applicationArguments, INPUT_FILE_PATH);
    outputFilePath = extractFirst(applicationArguments, OUTPUT_FILES_PATH);
    chunkSize = Integer.valueOf(extractFirst(applicationArguments, CHUNK_SIZE));
    recoveryMode = Boolean.valueOf(extractFirst(applicationArguments, RECOVERY_MODE));
  }

  private String extractFirst(ApplicationArguments args, CommandlineParam commandlineParam) {
    try {
      return args.getOptionValues(commandlineParam.getParamName()).get(0);
    } catch (Exception ex) {
      if (commandlineParam.getDefaultValue() != null) {
        return commandlineParam.getDefaultValue();
      }
      throw new RuntimeException("Failed to parse param: " + commandlineParam.getParamName(), ex);
    }
  }

  public String getInputFilePath() {
    return inputFilePath;
  }

  public String getOutputFilePath() {
    return outputFilePath;
  }

  public int getChunkSize() {
    return chunkSize;
  }

  public boolean recoveryMode() {
    return recoveryMode;
  }

}
