package com.ebay.catalogs.images.zoomformatter.repository.dataobjects;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;
import javax.persistence.Table;

@Entity
@Table(name = "media_repo")
//extends TimestampedEntity
public class MediaRepoDO  {
	
	private long id;
	private String ebayUrl;
	private String md5;
	private String providerId;
	private Integer width;
	private Integer height;
	private String copyright;
	private String subCopyright;
	private String sourceUrl;
	private String analysisData;
	
	public MediaRepoDO() {
		
	}
	
	public MediaRepoDO(long id, String ebayUrl, String md5, String providerId, Float score, Integer width, Integer height, String copyright,
			String subCopyright, String sourceUrl, String analysisData) {
		this.id = id;
		this.ebayUrl = ebayUrl;
		this.md5 = md5;
		this.providerId = providerId;
		this.width = width;
		this.height = height;
		this.copyright = copyright;
		this.subCopyright = subCopyright;
		this.sourceUrl = sourceUrl;
		this.analysisData = analysisData;
	}
	
	@Id
	@Column(name = "id", nullable = false)
	@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "SEQ_GEN")
	// TODO: can the allocationSize come as a bean, from config?
	@SequenceGenerator(name = "SEQ_GEN", sequenceName = "MEDIA_REPO_SEQ", allocationSize = 1000)
	public long getId() {
		return id;
	}
	
	public void setId(long id) {
		this.id = id;
	}
	
	@Column(name = "ebay_url", nullable = false)
	public String getEbayUrl() {
		return ebayUrl;
	}
	
	public void setEbayUrl(String ebayUrl) {
		this.ebayUrl = ebayUrl;
	}
	
	@Column(name = "media_md5", nullable = false)
	public String getMd5() {
		return md5;
	}
	
	public void setMd5(String md5) {
		this.md5 = md5;
	}
	
	@Column(name = "provider", nullable = false)
	public String getProviderId() {
		return providerId;
	}
	
	public void setProviderId(String providerId) {
		this.providerId = providerId;
	}
	
	@Column(name = "width", nullable = true)
	public Integer getWidth() {
		return width;
	}
	
	public void setWidth(Integer width) {
		this.width = width;
	}
	
	@Column(name = "height", nullable = true)
	public Integer getHeight() {
		return height;
	}
	
	public void setHeight(Integer height) {
		this.height = height;
	}
	
	@Column(name = "copyright", nullable = false)
	public String getCopyright() {
		return copyright;
	}
	
	public void setCopyright(String copyright) {
		this.copyright = copyright;
	}
	
	@Column(name = "SUB_COPYRIGHT", nullable = true)
	public String getSubCopyright() {
		return subCopyright;
	}
	
	public void setSubCopyright(String subCopyright) {
		this.subCopyright = subCopyright;
	}
	
	@Column(name = "source_url", nullable = false)
	public String getSourceUrl() {
		return sourceUrl;
	}
	
	public void setSourceUrl(String sourceUrl) {
		this.sourceUrl = sourceUrl;
	}
	
	@Column(name = "analysis_data", nullable = true)
	public String getAnalysisData() {
		return analysisData;
	}
	
	public void setAnalysisData(String analysisData) {
		this.analysisData = analysisData;
	}
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = (prime * result) + ((analysisData == null) ? 0 : analysisData.hashCode());
		result = (prime * result) + ((copyright == null) ? 0 : copyright.hashCode());
		result = (prime * result) + ((ebayUrl == null) ? 0 : ebayUrl.hashCode());
		result = (prime * result) + ((height == null) ? 0 : height.hashCode());
		result = (prime * result) + (int) (id ^ (id >>> 32));
		result = (prime * result) + ((md5 == null) ? 0 : md5.hashCode());
		result = (prime * result) + ((providerId == null) ? 0 : providerId.hashCode());
		result = (prime * result) + ((sourceUrl == null) ? 0 : sourceUrl.hashCode());
		result = (prime * result) + ((subCopyright == null) ? 0 : subCopyright.hashCode());
		result = (prime * result) + ((width == null) ? 0 : width.hashCode());
		return result;
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null) {
			return false;
		}
		if (getClass() != obj.getClass()) {
			return false;
		}
		MediaRepoDO other = (MediaRepoDO) obj;
		if (analysisData == null) {
			if (other.analysisData != null) {
				return false;
			}
		} else if (!analysisData.equals(other.analysisData)) {
			return false;
		}
		if (copyright == null) {
			if (other.copyright != null) {
				return false;
			}
		} else if (!copyright.equals(other.copyright)) {
			return false;
		}
		if (ebayUrl == null) {
			if (other.ebayUrl != null) {
				return false;
			}
		} else if (!ebayUrl.equals(other.ebayUrl)) {
			return false;
		}
		if (height == null) {
			if (other.height != null) {
				return false;
			}
		} else if (!height.equals(other.height)) {
			return false;
		}
		if (id != other.id) {
			return false;
		}
		if (md5 == null) {
			if (other.md5 != null) {
				return false;
			}
		} else if (!md5.equals(other.md5)) {
			return false;
		}
		if (providerId == null) {
			if (other.providerId != null) {
				return false;
			}
		} else if (!providerId.equals(other.providerId)) {
			return false;
		}
		if (sourceUrl == null) {
			if (other.sourceUrl != null) {
				return false;
			}
		} else if (!sourceUrl.equals(other.sourceUrl)) {
			return false;
		}
		if (subCopyright == null) {
			if (other.subCopyright != null) {
				return false;
			}
		} else if (!subCopyright.equals(other.subCopyright)) {
			return false;
		}
		if (width == null) {
			if (other.width != null) {
				return false;
			}
		} else if (!width.equals(other.width)) {
			return false;
		}
		return true;
	}
	
}
