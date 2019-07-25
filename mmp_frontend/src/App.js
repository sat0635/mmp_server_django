import React, { Component } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import ListSubheader from '@material-ui/core/ListSubheader';
import IconButton from '@material-ui/core/IconButton';
import InfoIcon from '@material-ui/icons/Info';
import Objects from './Objects';
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


class App  extends Component {
    state={
        posts:[],
    };  
    
     async componentDidMount() {
        setInterval(async () => {
        try {
            const res = await fetch('http://106.10.35.40:8000/api/picture/');
            const posts = await res.json();
            this.setState({
                posts,
            });

        } catch (e) {
            console.log("cannot fetch the REST API");
        }

       }, 1000);
    }

    render() {
        return  (  
		<div>
			<Objects posts={this.state.posts}/>
		</div>
	)
    }
}


export default App;
