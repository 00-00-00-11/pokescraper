package com.ebay.catalogs.r12npecomperator.file.input;

import java.io.IOException;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class InputFileReader {

  private static final String PATTERN = "\\d+";
  private final Pattern lineMatcher;

  public InputFileReader() {
    lineMatcher = Pattern.compile(PATTERN);
  }

  public Stream<Long> readEpids(URI fileName) {
    try {
      return Files.lines(Paths.get(fileName), StandardCharsets.UTF_8).map(this::processLine).filter(this::isValidLine)
          .map(this::extractEpid);
    } catch (IOException e) {
      throw new RuntimeException("Failed to open file " + fileName, e);
    }
  }

  private Long extractEpid(Matcher matcher) {
    return Long.valueOf(matcher.group());
  }

  private Matcher processLine(String line) {
    return lineMatcher.matcher(line);
  }

  private boolean isValidLine(Matcher matcher) {
    return matcher.find();
  }
}
