import React, {Component} from 'react'

import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import ListSubheader from '@material-ui/core/ListSubheader';
import IconButton from '@material-ui/core/IconButton';
import InfoIcon from '@material-ui/icons/Info';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
  },
  gridList: {
    width: 500,
    height: 450,
  },
  icon: {
    color: 'rgba(255, 255, 255, 0.54)',
  },
}));


const Exercises = props =>{
		 const classes = useStyles()
			
			return(
			<div className={classes.root}>
      <GridList cellHeight={180} className={classes.gridList}>
        <GridListTile key="Subheader" cols={2} style={{ height: 'auto' }}>
          <ListSubheader component="div">MMP 인증샷 갤러리 관리자 페이지</ListSubheader>
        </GridListTile>
        {props.posts.map(tile => (
          <GridListTile key={tile.IMAGE}>
            <img src={tile.IMAGE} alt={tile.TITLE} />
            <GridListTileBar
              title={tile.TITLE}
              subtitle={<span>by: {tile.CONTENT}</span>}
              actionIcon={
                <IconButton aria-label={`info about ${tile.TITLE}`} className={classes.icon}>
                  <InfoIcon />
                </IconButton>
              }
            />
          </GridListTile>
        ))}
      </GridList>
    </div>

                        )
	
	}


export default Exercises;
