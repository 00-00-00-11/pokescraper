/*
package com.ebay.catalogs.images.zoomformatter.repository.dataobjects;

import com.ebay.catalogs.muse.logic.db.util.DateType;
import java.util.Date;
import javax.persistence.Column;
import javax.persistence.MappedSuperclass;
import javax.persistence.PreUpdate;
import org.hibernate.annotations.Type;
import org.hibernate.annotations.TypeDef;
import org.hibernate.annotations.TypeDefs;

@MappedSuperclass
@TypeDefs({ @TypeDef(name = DateType.TYPE, typeClass = DateType.class) })
public class TimestampedEntity {
	
	private Date created;
	private Date modified;
	
	public TimestampedEntity() {
		// MySql datetime precision is only up to a second. Java Date precision is up to a millisecond.
		// Date date = DateUtils.truncate(new Date(), Calendar.SECOND);
		created = modified = new Date();
	}
	
	@PreUpdate
	public void onUpdate() {
		modified = new Date();
	}
	
	@Type(type = DateType.TYPE)
	@Column(name = "creation_date", nullable = false, updatable = false)
	public Date getCreated() {
		return created;
	}
	
	public void setCreated(Date created) {
		this.created = created;
	}
	
	@Type(type = DateType.TYPE)
	@Column(name = "last_modified_date", nullable = false)
	public Date getModified() {
		return modified;
	}
	
	public void setModified(Date modified) {
		this.modified = modified;
	}
	
}*/
